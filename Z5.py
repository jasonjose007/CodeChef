# Beginning Zeros
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    input_data = sys.stdin.read().split()
    for s in input_data:
        print(len(s) - len(s.lstrip('0')))

if __name__ == '__main__':
    main()