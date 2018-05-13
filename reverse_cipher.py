# Reverse Cipher
# https://nostarch.com/crackingcodes/ (BSD License)

message = input('Enter message: ')

# while loop method
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

# extended slice method
#translated = message[::-1]

# reversed() built-in function method
#translated = "".join(reversed(message))

print(translated)
