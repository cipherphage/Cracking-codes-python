# this is the main entry point
# handles initial main menu and user input

# local modules
from reverse_cipher import reverseCipher
from caesar_cipher import caesarCipher
from caesar_brute_force import caesarBruteForce
from transposition_cipher import transpositionCipher
from transposition_brute_force import transpositionBruteForce
# from transposition_file_cipher import transpositionCipherFile

def main():
    # main menu options
    options = ['a','b','c','d','e']
    # main menu string
    menu = ('Ciphers:\n'
        'A) Reverse message cipher (encrypt/decrypt)\n'
        'B) Caesar message cipher (encrypt/decrypt)\n'
        'C) Caesar message brute forcer\n'
        'D) Transposition message cipher (encrypt/decrypt)\n'
        'E) Transposition message brute forcer\n'
        # 'F) Transposition file cipher (encrypt/decrypt)\n'  # not completed yet
        'Type the letter of the one you want:'
    )

    # cipher to use, lowercased to streamline checking
    choice = input(menu).lower()

    if choice not in options:
        print(f'Invalid choice: {choice}. Please try again.')
        return main()

    # string to be encrypted/decrypted
    message = input('Enter message: ')

    if choice in ['b','d']:
        # whether the program enc or dec, lowercased to streamline checking
        # note: reverse cipher doesn't need this check, just run the cipher
        mode = input('Type e for encrypt or d for decrypt: ').lower()

        if mode not in ['e','d']:
            print(f'Invalid choice: {choice}. Please try again.')
            return main()
    
    if choice == 'a':
        reverseCipher(message)
    elif choice == 'b':
        caesarCipher(mode, message)
    elif choice == 'c':
        caesarBruteForce(message)
    elif choice == 'd':
        transpositionCipher(mode, message)
    elif choice == 'e':
        transpositionBruteForce(message)
    # elif choice == 'f':
    #   transpositionCipherFile()


if __name__ == '__main__':
    main()