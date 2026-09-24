# Water Consumption
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    for i in range(1, T + 1):
        X = int(input_data[i])
        if X >= 2000:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()