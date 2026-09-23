# Alice and Marks
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    X = int(input_data[0])
    Y = int(input_data[1])
    if X >= 2 * Y:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()