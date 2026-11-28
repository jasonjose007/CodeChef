# CRED Coins
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Basic Math

import sys

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        print((x * y) // 100)

if __name__ == '__main__':
    main()