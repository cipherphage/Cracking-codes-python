# Caesar Cipher

import pyperclip

# the string to be encrypted/decrypted
message = input('Enter message: ')

# the enc/dec key
key = 13

# whether the program enc or dec
mode = input('Type e for encrypt or d for decrypt: ')

# every possible symbol that can be enc:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,'

# store the enc/dec message:
translated = ''

# main caesar cipher algorithm
for symbol in message:
    # if the symbol is valid then handle encryption/decryption
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if (mode == 'e' or mode == 'E'):
            translatedIndex = symbolIndex + key
        elif (mode == 'd' or mode == 'D'):
            translatedIndex = symbolIndex - key
        else:
            print('Mode ' + mode + ' not recognized.  Must be the letter e or the letter d, case insensitive.')

        # handle wraparound
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # notify user of non-encrypted/decrypted symbols
        print('Warning: the symbol ' + symbol + ' is left untouched by this cipher.')

        # append the raw symbol
        translated = translated + symbol

# output the result
print('The following result has also been copied to your clipboard: ')
print(translated)
pyperclip.copy(translated)

