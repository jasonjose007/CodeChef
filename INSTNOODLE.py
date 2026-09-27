# Chef and Instant Noodles
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Basic Math

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    X = int(input_data[0])
    Y = int(input_data[1])
    print(X * Y)

if __name__ == '__main__':
    solve()