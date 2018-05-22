# transposition brute force

import math
import pyperclip


def main():
    myMessage = input('Enter message: ')
    # should add a check to make sure message len > 7
    myKeyMax = int(len(myMessage) / 2)

    # create list of potential decrypted messages
    forcedList = decryptMessage(myKeyMax, myMessage)

    # allow user to copy a particular message to clipboard
    copier(forcedList)


def copier(messages):
    # prompt for copying by key
    copyMessageInput = input('Enter key of message to copy: ')
    copyMessage = messages[int(copyMessageInput) - 2]
    if (copyMessage):
        pyperclip.copy(copyMessage)
    else:
        print(copyMessageInput + ' is an invalid key.  Please try again.')
        copier(messages)


def printForcedText(key, text):
    # convert key from int to str
    # add 0 in front of single digits for clarity
    if (key < 10):
        key = '0' + str(key)
    else:
        key = str(key)

    # print with key at beginning and a | at the end
    print(key + ': ' + text + '|')


def decryptMessage(keyRange, message):
    messageList = []

    for key in range(2, keyRange):
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

        #print message, then append to master list
        newMessage = ''.join(plaintxt)
        printForcedText(key, newMessage)
        messageList.append(newMessage)

    return messageList


if __name__ == '__main__':
    main()
