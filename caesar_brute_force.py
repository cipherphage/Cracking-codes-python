# Caesar Cipher Brute Force Hacker

import pyperclip

message = input('Enter the encrypted message to brute force: ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,`~@#$%^&*()_-+=[]{}|;:<>/'

# store undec symbols
unaccepted = ''

# list of results
results = []

# count for iterations
count = 0

# loop through every possible key
for key in range(len(SYMBOLS)):
    # store translated message
    translated = ''

    # main caesar cipher algorithm
    for symbol in message:
        # if the symbol is valid then handle decryption
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # handle wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # append non-decrypted symbols for warning message
            unaccepted = unaccepted + symbol

            # append the raw symbol to the message
            translated = translated + symbol

    # store the result
    results.append(translated)

    # output the result
    # warn of undecrypted symbols
    if count == 0:
        if len(unaccepted) > 0:
            print(f'* * * * Warning * * * * \nThese symbols were not decrypted: {unaccepted}\n* * * * * * * * * * * *')

    # prettify the number for clarity
    if len(str(count)) == 1:
        num = '0' + str(count)
    else:
        num = str(count)

    print(num + ': ' + translated)

    # count the iteration afterward
    count += 1

# afterward ask the user to choose to copy one of the results
indexToCopy = input('Type the key of the message you\'d like to copy to your clipboard: ')
messageToCopy = results[int(indexToCopy)]
print(f'Message with key {indexToCopy} has been copied to your clipboard:')
print(messageToCopy)
pyperclip.copy(messageToCopy)

