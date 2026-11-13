# Tax in Chefland
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

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
        if x > 100:
            out.append(str(x - 10))
        else:
            out.append(str(x))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()