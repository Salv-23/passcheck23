
Welcome to passcheck
====================

**passcheck** uses the API from `haveibeenpwned.com <https://haveibeenpwned.com/>`_,
specifically the method to search compromised passwords with a range. It first converts your password to a SHA-1 password
and uses the first 5 characters (prefix) to search the database of haveibeenpwned. ::

 - GET https://api.pwnedpasswords.com/range/{first 5 hash chars}

The API returns a list of SHA-1 suffixes
(the remaining 35 characters of a SHA-1 password) that match your prefix and the times it has been compromised. ::

 - 0018A45C4D1DEF81644B54AB7F969B88D65:1
 - 00D4F6E8FA6EECAD2A3AA415EEC418D38EC:2
 - 011053FD0102E94D6AE2F8B83D76FAF94F6:1
 - 012A7CA357541F0AC487871FEEC1891C49C:2
 - 0136E006E24E7D152139815FB0FC6A50B15:2
 - ...

We then search if there's a matching suffix to our password and return the times it has been compromised.
For more information about this method you can check the `haveibeenpwned API <https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange>`_.

Example of use:
---------------

You can execute passcheck and write the password(s) as argument(s). ::

    python3 -m passcheck password123 safe69 cheetosflaming_hot

Output::

 Checking your password(s)...
 'password123' has been compromised 126927 times, you should consider changing it.
 'safe69' has been compromised 153 times, you should consider changing it.
 'cheetosflaming_hot' hasn't been compromised.
 Done!

Or you can import passcheck.search and use main::

    from passcheck import search
    search.main(['helloworld', 'strongpass', 'ivermectin'])

output::

    Checking your password(s)...
    'helloworld' has been compromised 16418 times, you should consider changing it.
    'strongpass' has been compromised 225 times, you should consider changing it.
    'ivermectin' has been compromised 17 times, you should consider changing it.
    Done!

