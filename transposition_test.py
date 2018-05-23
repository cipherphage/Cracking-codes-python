# transposition cipher test

import random, sys
import transposition_cipher, transposition_brute_force


def main():
    random.seed(43)

    for i in range(101):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,`~@#$%^&*()_-+=[]{}|;:<>/' * random.randint(2, 42)

        # convert message str to list
        message = list(message)
        random.shuffle(message)
        #convert back to str
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # check all possible keys for each message

