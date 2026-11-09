# Captain needs new Heliwings
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

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
        
        current_max = 0
        total_points = 0
        
        for _ in range(N):
            level = int(data[idx])
            idx += 1
            if level > current_max:
                total_points += level
                current_max = level
                
        out.append(str(total_points))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()