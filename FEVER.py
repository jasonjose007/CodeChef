# Fever
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
    for i in range(1, t + 1):
        x = int(data[i])
        if x > 98:
            out.append("YES")
        else:
            out.append("NO")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()