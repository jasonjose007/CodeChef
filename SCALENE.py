# Scalene Triangle
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
    for i in range(1, 3 * t + 1, 3):
        a = int(data[i])
        b = int(data[i+1])
        c = int(data[i+2])
        
        if a != b and b != c and a != c:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()