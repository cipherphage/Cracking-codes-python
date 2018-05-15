# Caesar Cipher

import pyperclip
import cipherrandom


def main():
    # the string to be encrypted/decrypted
    message = input('Enter message: ')

    # whether the program enc or dec
    mode = input('Type e for encrypt or d for decrypt: ')

    # every possible symbol that can be enc:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,`~@#$%^&*()_-+=[]{}|;:<>/'
    symLength = len(SYMBOLS)

    # check for random key
    if mode == 'e' or mode == 'E':
        key = cipherrandom.getRandInt(symLength)
    else:
        keyInput = input('Input key to decrypt by: ')
        key = int(keyInput)

        # check key is legit
        if key < 0 or key >= symLength:
            print('Your key must be between 0 and ' + (symlength - 1))
            return main()

    # store the enc/dec message:
    translated = ''

    # store unenc/undec symbols
    unaccepted = ''

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
            # append non-encrypted/decrypted symbols for warning message
            unaccepted = unaccepted + symbol

            # append the raw symbol to the message
            translated = translated + symbol

    # output the result
    if len(unaccepted) > 0:
        print('* * * * Warning * * * * \nThese symbols were untouched by the Caesar Cipher: ' + unaccepted + '\n* * * * * * * * * * * *')

    print('Your key is: ' + str(key))
    print('The following result has been copied to your clipboard: ')
    print(translated)
    pyperclip.copy(translated)


if __name__ == '__main__':
    main()

