# How many unattempted problems
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    M = int(input_data[0])
    R = int(input_data[1])
    MOD = 1000000007
    print((M - R) % MOD)

if __name__ == '__main__':
    solve()