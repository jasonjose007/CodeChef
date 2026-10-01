# Greater Average
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    T = int(data[0])
    results = []
    idx = 1
    
    for _ in range(T):
        A = float(data[idx])
        B = float(data[idx+1])
        C = float(data[idx+2])
        idx += 3
        
        avg = (A + B) / 2
        if avg > C:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()