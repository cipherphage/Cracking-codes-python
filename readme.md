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

- I have modified, sometimes heavily, the examples from the book.
- [Original Cracking Codes examples are under a BSD License.][1]
- pyperclip.py is a utility module for interfacing with an OS's clipboard.
    - It was written by the author of [Cracking Codes with Python][1].
    - It is a security risk due to the fact that any program could use it to access your clipboard.
    - All of the scripts can be used without the pyperclip module by simply commenting it out in each script.
- Python 3 is used through-out.
- THE CIPHERS HERE ARE NOT CRYPTOGRAPHICALLY SECURE.  DON'T USE THEM.  THIS IS FOR LEARNING AND FUN, DUDE, SRSLY.

[1]:https://www.nostarch.com/crackingcodes/
