# ATM Machine
# Platform: CodeChef
# Difficulty: Medium
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
        K = int(data[idx+1])
        idx += 2
        
        res = []
        for i in range(N):
            A = int(data[idx + i])
            if K >= A:
                K -= A
                res.append('1')
            else:
                res.append('0')
        idx += N
        out.append("".join(res))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()