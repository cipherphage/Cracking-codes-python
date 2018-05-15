# transposition cipher

import pyperclip
import secrets
import cipherrandom


def main():
    myMessage = input('Enter message: ')
    msgLength = len(myMessage)

    # message must be more than 7 characters long
    # otherwise transposition won't happen mathematically
    if msgLength <= 7:
        print('Message length must be more than 7 characters!')
        return main()

    myKey = cipherrandom.getRandTransInt(msgLength)
    ciphertext = encryptMessage(myKey, myMessage, msgLength)

    # print key
    print('Your key is: ' + str(myKey))
    # print encrypted string with | at end to indicate end
    print('Your encrypted message is: ' + ciphertext + '|')
    pyperclip.copy(ciphertext)


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


# if transposition cipher is run call main
if __name__ == '__main__':
    main()
