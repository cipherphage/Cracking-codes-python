# My repo for [Cracking Codes with Python][1]

## Ciphers

- reverse cipher (reverse_cipher.py)
- caesar cipher (caesar_cipher.py)

## Hacks

- caesar cipher brute force (caesar_brute_force.py)

## Utilities

- clipboard module (pyperclip.py) 
    - please see important note below.

## Notes and Important Warnings

- I have slightly modified the examples in the book.
- [Cracking Codes examples are under a BSD License.][1]
- pyperclip.py is a utility module for interfacing with an OS's clipboard.
    - It was written by the author of [Cracking Codes with Python][1].
    - It is a security risk due to the fact that any program could use it to access your clipboard.
    - All of the scripts can be used without the pyperclip module by simply commenting it out in each script.
- Python 3 is used through-out.

[1]:https://www.nostarch.com/crackingcodes/
