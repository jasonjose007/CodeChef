# Read Pages
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts, Mathematics

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        x = int(input_data[idx+1])
        y = int(input_data[idx+2])
        idx += 3
        
        if x * y >= n:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()