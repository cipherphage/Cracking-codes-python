# transposition cipher

# built-in modules
import math
# 3rd party modules
import pyperclip
# local modules
import cipher_random, cipher_main


def transpositionCipher(mode, myMessage):
    msgLength = len(myMessage)

    # check encrypt or decrypt
    if mode == 'e':
        # message must be more than 7 characters long
        # otherwise transposition won't happen mathematically
        if msgLength <= 7:
            print('Message length must be more than 7 characters!')
            return cipher_main.main()

        myKey = cipher_random.getRandTransInt(msgLength)
        ciphertext = encryptMessage(myKey, myMessage, msgLength)

        # print key
        print(f'Your key is: {str(myKey)}')
        # print encrypted string
        print(f'Your encrypted message is: {ciphertext}')
        pyperclip.copy(ciphertext)
        print('Your encrypted message has been copied to your clipboard.')
    else:
        # get user input key
        try:
            myKey = int(input('Enter key: '))
        except ValueError:
            print('Key must be a number.  Please try again.')
            return cipher_main.main()
        
        # check key is legit
        if myKey < 0 or myKey >= msgLength:
            print(f'Your key must be between 0 and {msgLength - 1}')
            return cipher_main.main()

        # get decrypted message
        decrypted = decryptMessage(myKey, myMessage)
        # print encrypted string
        print(f'Your decrypted message is: {decrypted}')
        pyperclip.copy(decrypted)
        print('Your decrypted message has been copied to your clipboard.')


def encryptMessage(key, message, msgLength):
    # each string is a column in the grid
    ciphertext = [''] * key

    # loop through each column in the ciphertext
    for column in range(key):
        currentIndex = column

        # loop until index goes past msg length
        while currentIndex < msgLength:
            # put the symbol at index in msg at end of column
            ciphertext[column] += message[currentIndex]

            # move current index
            currentIndex += key

    # convert the ciphertext list into a str and return
    return ''.join(ciphertext)

def decryptMessage(key, message):
    newMessage = decrypter(key, message)
    return newMessage


def decrypter(key, message):
    # num of cols in transposition grid
    numOfCols = int(math.ceil(len(message) / float(key)))

    # num of rows in grid
    numOfRows = key

    # num of 'shaded boxes' in last col of grid
    numOfShadedBoxes = (numOfCols * numOfRows) - len(message)

    # each str in plaintxt is a col in the grid
    plaintxt = [''] * numOfCols
    col = 0
    row = 0

    for symbol in message:
        plaintxt[col] += symbol
        col += 1

        # if no more cols or at shaded box go back to first col
        if (col == numOfCols) or (col == numOfCols - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    # return decrypted message
    return ''.join(plaintxt)
