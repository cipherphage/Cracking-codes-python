# transposition brute force

import math
import pyperclip


def main():
    userChoice = input('Type a for brute force or b for decryption: ')

    if userChoice == 'a' or userChoice == 'A':
        userChoice = True
        print('You chose brute force.')
    elif userChoice == 'b' or userChoice == 'B':
        userChoice = False
        print('You chose decryption.')
    else:
        print('Error: unknown choice ' + userChoice + '.')
        main()

    myMessage = input('Enter message: ')
    # should add a check to make sure message len > 7

    if userChoice:
        myKeyMax = int(len(myMessage) / 2)
        # create list of potential decrypted messages
        decrypted = bruteForceMessage(myKeyMax, myMessage)
    else:
        # get user input key
        myKey = input('Enter key: ')
        # add check for valid key here
        # get decrypted message
        decrypted = decryptMessage(int(myKey), myMessage)

    # allow user to copy a particular message to clipboard
    copier(decrypted)


def copier(messages):
    if type(messages) is list:
        # prompt for copying by key
        copyMessageInput = input('Enter key of message to copy: ')
        copyMessage = messages[int(copyMessageInput) - 2]
        if (copyMessage):
            pyperclip.copy(copyMessage)
            print('Your decrypted message at key ' + copyMessageInput + ' has been copied to your clipboard.')
        else:
            print(copyMessageInput + ' is an invalid key.  Please try again.')
            copier(messages)
    else:
        pyperclip.copy(messages)
        print('Your decrypted message has been copied to your clipboard.')


def printForcedText(key, text):
    # convert key from int to str
    # add 0 in front of single digits for clarity
    if (key < 10):
        key = '0' + str(key)
    else:
        key = str(key)

    # print with key at beginning and a | at the end
    print(key + ': ' + text + '|')


def bruteForceMessage(keyRange, message):
    messageList = []

    for key in range(2, keyRange):
        newMessage = decrypter(key, message)
        printForcedText(key, newMessage)
        messageList.append(newMessage)
    return messageList



def decryptMessage(key, message):
    newMessage = decrypter(key, message)
    printForcedText(key, newMessage)
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



if __name__ == '__main__':
    main()
