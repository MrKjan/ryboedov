# Write a program in any programming language that counts backwards from value
# provided by user to 1 and prints:
# “Agile” if the number is divisible by 5,
# “Software” if the number is divisible by 3,
# “Testing” if the number is divisible by both,
# or prints just the number if none of those cases are true.

import sys


if __name__ == "__main__":
    for val in reversed(range(1, int(sys.argv[1]) + 1)):
        if val % 3 == 0 and val % 5 == 0:
            print('Testing')
        elif val % 5 == 0:
            print('Agile')
        elif val % 3 == 0:
            print('Software')
        else:
            print(val)
