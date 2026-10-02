# Find maximum in an Array
# Platform: CodeChef
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    T = int(data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        
        max_height = 0
        for _ in range(N):
            height = int(data[idx])
            idx += 1
            if height > max_height:
                max_height = height
                
        out.append(str(max_height))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()