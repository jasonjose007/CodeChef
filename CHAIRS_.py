# Chairs Requirement
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Algorithms

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
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        if x > y:
            out.append(str(x - y))
        else:
            out.append("0")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()