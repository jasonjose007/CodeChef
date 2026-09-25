# Biryani classes
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    out = []
    idx = 1
    for _ in range(T):
        X = int(input_data[idx])
        Y = int(input_data[idx+1])
        idx += 2
        out.append(str(X * Y))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()