# Increase IQ
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    X = int(input_data[0])
    if X + 7 > 170:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()