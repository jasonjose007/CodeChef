# Cricket World Cup Qualifier
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    X = int(data[0])
    if X >= 12:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()