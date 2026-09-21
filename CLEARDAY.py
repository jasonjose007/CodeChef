# Clear Day
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
    print(7 - X - Y)

if __name__ == '__main__':
    solve()