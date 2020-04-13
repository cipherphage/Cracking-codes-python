# My repo for [Cracking Codes with Python][1]

## Ciphers

- reverse cipher (reverse_cipher.py)
- caesar cipher (caesar_cipher.py)
- transposition cipher (transposition_cipher.py)

## Hacks

- caesar cipher brute force (caesar_brute_force.py)
- transposition cipher brute force (transposition_brute_force.py)

## Utilities

- Clipboard module (pyperclip.py)
    - It was written by the author of [Cracking Codes with Python][1] and is not modified by me.
- Random numbers utilizing Python 3's secrets module (cipherrandom.py)
    - I wrote these helper functions.
    - Secrets uses the most secure sources of randomness your OS provides.
    - On some modern and up-to-date OSes this randomness is cryptographically secure.
    - That does not mean the cipher is cryptographically secure.

## Tests

- transposition encrypt/decrypt test (transposition_test.py)

## Notes and Important Warnings

- PEP-506 has some important notes regarding random numbers used in a security context:  
  Although the documentation for the random module explicitly states that the default is not suitable for security purposes, it is strongly believed that this warning may be missed, ignored or misunderstood by many Python developers. In particular:

    - developers may not have read the documentation and consequently not seen the warning;
    - they may not realise that their specific use of the module has security implications; or
    - not realising that there could be a problem, they have copied code (or learned techniques) from websites which don't offer best practises.
  
  The first hit when searching for "python how to generate passwords" on Google is a tutorial that uses the default functions from the random module. Although it is not intended for use in web applications, it is likely that similar techniques find themselves used in that situation. The second hit is to a StackOverflow question about generating passwords. Most of the answers given, including the accepted one, use the default functions. When one user warned that the default could be easily compromised, they were told "I think you worry too much."
- Read PEP-506 here: [https://www.python.org/dev/peps/pep-0506/][2]. It specifies the new secrets module which was added to Python in verion 3.6.  The secrets module is what should be used when cryptographically secure pseudo random numbers are required.
- I have modified, sometimes heavily, the examples from the book.
- [Original Cracking Codes examples are under a BSD License.][1]
- pyperclip.py is a utility module for interfacing with an OS's clipboard.
    - It was written by the author of [Cracking Codes with Python][1].
    - It is a security risk due to the fact that any program could use it to access your clipboard.
    - All of the scripts can be used without the pyperclip module by simply commenting it out in each script.
- Python 3 is used through-out.
- THE CIPHERS HERE ARE NOT CRYPTOGRAPHICALLY SECURE.  DON'T USE THEM.  THIS IS FOR LEARNING AND FUN.

[1]:https://www.nostarch.com/crackingcodes/
[2]:https://www.python.org/dev/peps/pep-0506/