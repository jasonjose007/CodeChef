# Candy Division
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts, Mathematics

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        if n % 3 == 0:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()