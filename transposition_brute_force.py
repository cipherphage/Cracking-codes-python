# transposition brute forcer

# built-in modules
import math
# 3rd party modules
import pyperclip
# local modules 
import transposition_cipher, cipher_main


def transpositionBruteForce(myMessage):
    myKeyMax = int(len(myMessage) / 2)
    # create list of potential decrypted messages
    decrypted = bruteForceMessage(myKeyMax, myMessage)
 
    # allow user to copy a particular message to clipboard
    copier(decrypted)

def copier(messages):
    # prompt for copying by key
    try:
        copyMessageInput = int(input('Enter key of message to copy: '))
    except ValueError:
        print('Key must be a number.  Please try again.')
        return cipher_main.main()
        
    copyMessage = messages[copyMessageInput - 2]
    if (copyMessage):
        pyperclip.copy(copyMessage)
        print(f'Your decrypted message at key {copyMessageInput} has '
            'been copied to your clipboard.')
    else:
        print(f'{copyMessageInput} is an invalid key.  Please try again.')
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


def bruteForceMessage(keyRange, message):
    messageList = []

    for key in range(2, keyRange):
        newMessage = transposition_cipher.decrypter(key, message)
        printForcedText(key, newMessage)
        messageList.append(newMessage)
    return messageList
