# transposition cipher test

# built-in modules
import random, sys
# local modules
import cipher_random, transposition_cipher, transposition_brute_force


def main():
    random.seed(43)

    for i in range(19):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk'
            'lmnopqrstuvwxyz1234567890 !?.,`~@#$%^&*()_-+=[]{}|;:<>/' 
        message = message * random.randint(2, 23)

        # convert message str to list
        message = list(message)
        random.shuffle(message)
        #convert back to str
        message = ''.join(message)

        # check all possible keys for each message
        for key in range(2, int(len(message) / 2)):
            encrypted = transposition_cipher.encryptMessage(key, message, \
                len(message))
            decrypted = transposition_cipher.decryptMessage(key, encrypted)

            # if results don't match then display error and quit
            if message != decrypted:
                print(f'{key} is not the correct key for message: {message}.')
                print(f'Decrypted as: {decrypted}')
                sys.exit()

        print(f'Test #{i+1} passed on message: "{message[:50]}..."')


if __name__ == '__main__':
    main()
