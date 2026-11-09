# Waiting Time
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        k = int(data[idx])
        x = int(data[idx+1])
        idx += 2
        out.append(str(k * 7 - x))
    
    print('\n'.join(out))

if __name__ == '__main__':
    solve()