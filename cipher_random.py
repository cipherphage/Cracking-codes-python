# collection of random number helpers
# written by cp

# built-in modules
import secrets


# get random int in range
def getRandInt(length):
    return secrets.randbelow(length)


# get random int in range for transposition
# this requires int greater than 1
def getRandTransInt(length):
    num = 0

    # convert length into useful int for transposition
    length = int(length / 2)

    # make sure num isn't 0 or 1
    while num < 2:
        num = getRandInt(length)

    return num
