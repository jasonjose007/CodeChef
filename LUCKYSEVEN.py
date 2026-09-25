# Lucky Seven
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    s = sys.stdin.readline().strip()
    if len(s) >= 7:
        print(s[6])

if __name__ == '__main__':
    main()