# Caesar Cipher

# 3rd party modules
import pyperclip
# local modules
import cipher_random, cipher_main


def caesarCipher(mode, message):
    # every possible symbol that can be enc:
    SYMBOLS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk'
        'lmnopqrstuvwxyz1234567890 !?.,`~@#$%^&*()_-+=[]{}|;:<>/')
    symLength = len(SYMBOLS)

    # check for random key
    if mode == 'e':
        key = cipher_random.getRandInt(symLength)
    else:
        try:
            key = int(input('Input key to decrypt by: '))
        except ValueError:
            print('Key must be a number.  Please try again.')
            return cipher_main.main()

        # check key is legit
        if key < 0 or key >= symLength:
            print(f'Your key must be between 0 and {symLength - 1}')
            return cipher_main.main()

    # store the enc/dec message:
    translated = ''

    # store unenc/undec symbols
    unaccepted = ''

    # main caesar cipher algorithm
    for symbol in message:
        # if the symbol is valid then handle encryption/decryption
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            if (mode == 'e'):
                translatedIndex = symbolIndex + key
            else:
                translatedIndex = symbolIndex - key

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
        print('Warning: These symbols were '
            f'untouched by the Caesar Cipher: {unaccepted}')

    print(f'Your key is: {str(key)}')
    print('The following result has been copied to your clipboard: ')
    print(translated)
    pyperclip.copy(translated)
