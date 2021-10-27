"""
Demo project: passcheck
~~~~~~~~~~~~~~~~~~~~~~~

This project serves mainly as practice for sphinx and apidoc implementation.

The idea is to take any amount of passwords from the user and verify if they've
been compromised using the API from `haveibeenpwned <https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange>`_
that uses a `k-Anonymity model <https://en.wikipedia.org/wiki/K-anonymity>`_
that allows passwords to be searched by a partial hash.

After converting the passwords to SHA-1 we use the API to verify any compromised password(s)
and print the results.
"""

__author__ = "Salvador Estrella"