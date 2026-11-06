# Valid Triangles
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Basic Math

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        A = int(input_data[idx])
        B = int(input_data[idx+1])
        C = int(input_data[idx+2])
        idx += 3
        
        if A + B + C == 180:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()