# Ezio and Guards
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        x = int(data[2 * i - 1])
        y = int(data[2 * i])
        if x >= y:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()