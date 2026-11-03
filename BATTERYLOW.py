# Battery Low
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    out = []
    for i in range(1, T + 1):
        X = int(input_data[i])
        if X <= 15:
            out.append("YES")
        else:
            out.append("NO")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()