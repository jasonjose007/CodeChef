# Decrement OR Increment
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def main():
    n = int(sys.stdin.read().strip())
    if n % 4 == 0:
        print(n + 1)
    else:
        print(n - 1)

if __name__ == '__main__':
    main()