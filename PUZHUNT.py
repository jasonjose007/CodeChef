# Puzzle Hunt
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    g = int(input_data[0])
    if 6 <= g <= 8:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()