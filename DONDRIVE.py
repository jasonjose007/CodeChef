# Donation Drive
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        x = int(input_data[idx+1])
        idx += 2
        print(n - x)

if __name__ == '__main__':
    solve()