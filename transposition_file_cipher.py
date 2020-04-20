# transposition cipher for files

# built-in modules
import time, os, sys
# local modules
import transposition_cipher, transposition_brute_force, cipher_random, \
    cipher_main

def transpositionCipherFile():
    inputPath = input("Enter the absolute path to the file to encrypt. \n "
        "Note: if you enter a path to a directory \n "
        "all of the directory's contents will be encrypted: ")

    # check file or dir exists
    if os.path.exists(inputPath):
        # handle dir
        if os.path.isdir(inputPath):
            directory = os.fsencode(inputPath)
            # loop over files in dir
            for file in os.listdir(directory):
                tEncryptFile(file)
        # handle file
        else:
            file = os.fsencode(inputPath)
            tEncryptFile(file)
    # if path doesn't exist offer chance to try again
    else:
        print("Path doesn't exist. Make sure it's an absolute path.")
        input("Press Enter to try again...\n")
        transpositionCipherFile()

def tEncryptFile(file):
    print(file)
    # outputFilename = 
    # fileLength = 
    # key = cipher_random.getRandTransInt(fileLength)
        
        
