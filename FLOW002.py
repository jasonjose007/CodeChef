# Find Remainder
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Algorithms

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
        A = int(data[idx])
        B = int(data[idx+1])
        results.append(str(A % B))
        idx += 2
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()