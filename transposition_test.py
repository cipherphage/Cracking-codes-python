# transposition cipher test

import random, sys
import cipherrandom
import transposition_cipher, transposition_brute_force


def main():
    random.seed(43)

    for i in range(19):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,`~@#$%^&*()_-+=[]{}|;:<>/' * random.randint(2, 23)

        # convert message str to list
        message = list(message)
        random.shuffle(message)
        #convert back to str
        message = ''.join(message)

        # check all possible keys for each message
        for key in range(2, int(len(message) / 2)):
            encrypted = transposition_cipher.encryptMessage(key, message, len(message))
            decrypted = transposition_brute_force.decryptMessage(key, encrypted)

            # if results don't match then display error and quit
            if message != decrypted:
                print('%s is not the correct key for message: %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

            print('Test #%s passed with key %s: "%s..."' % (i+1, key, message[:50]))


if __name__ == '__main__':
    main()
