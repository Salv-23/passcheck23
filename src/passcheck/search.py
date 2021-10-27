"""
    search.py
    ---------

    This module contains all the functions to convert a string to a SHA-1 password and
    use the haveibeenpwned API to see whether the password(s) has been compromised.
    It also contains the __main__ construct to make the module executable.
"""

__author__ = "Salvador Estrella"

import hashlib
import requests
import sys


def request_api_data(prefix):
    """
    Fetches the response of pwnedpasswords-API using a prefix.

    :param prefix: The first 5 characters of a SHA-1 password hash (not case sensitive).
    :return: A list of suffixes that match our prefix and a count of the times it has
            been compromised e.g. 00D4F6E8FA6EECAD2A3AA415EEC418D38EC:2.
    :raise RuntimeError: If API returns any HTTP code different to 200, e.g. HTTP 404.
    """
    url = "https://api.pwnedpasswords.com/range/" + prefix
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching {response.status_code}. check the API and try again")
    return response


def count_password_leaked(hashes, hash_to_check):
    """
    Checks if there's any hash suffix in the response passed by :func:`request_api_data`
    that matches the suffix of our password(s) we get from :func:`pawned_api_check`.

    :param hashes: The response we get from :func:`request_api_data`
    :param hash_to_check: The hash suffix from our password(s) we get from :func:`pawned_api_check`.
    :return: If there's any matching suffix returns the count of times it has been compromised
            otherwise returns 0.
    """
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def pawned_api_check(password):
    """
    Converts password(s) to SHA-1 hash and splits it into suffix(first 5 characters) and
    prefix(remaining 35 characters). Invokes both :func:`request_api_data` and :func:`count_password_leaked`.

    :param password: The password we want to use
    :return: The count from :func:`count_password_leaked`
    """
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    suffix, prefix = sha1password[:5], sha1password[5:]
    response = request_api_data(suffix)
    return count_password_leaked(response, prefix)


def main(args) -> None:
    """
    Iterates over a list of passwords strings and checks whether any of them has been compromised,
    then prints the results. Two guard clauses are included to prevent misfunction.

    :param args: A list of strings
    :return: None
    :raise ValueError: If args is not a list or members of args are not strings.
    """
    if not isinstance(args, list):
        raise ValueError("Passwords must be contained in a list")

    for password in args:
        if not isinstance(password, str):
            raise ValueError("Passwords must be strings in order to convert them to a SHA-1 hash")

    print("Checking your password(s)...")
    for password in args:
        count = pawned_api_check(password)
        if count:
            print(f"'{password}' has been compromised {count} times, you should consider changing it.")
        else:
            print(f"'{password}' hasn't been compromised.")
    print("Done!")


if __name__ == "__main__":
    main(sys.argv[1:])

