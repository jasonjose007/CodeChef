# Course Registration
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts, Mathematics, Basic Math

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        N = int(input_data[idx])
        M = int(input_data[idx+1])
        K = int(input_data[idx+2])
        idx += 3
        
        if N + K <= M:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()