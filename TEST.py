# Life, the Universe, and Everything
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        num = int(line)
        if num == 42:
            break
        print(num)

if __name__ == '__main__':
    main()