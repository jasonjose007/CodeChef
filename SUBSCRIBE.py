# Get Subscription
# Platform: CodeChef
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    out = []
    for _ in range(T):
        X = int(input_data[idx])
        idx += 1
        if X > 30:
            out.append("YES")
        else:
            out.append("NO")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()