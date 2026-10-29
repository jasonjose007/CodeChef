# Escape the Grid
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    MOD = 1000000007
    
    T = int(data[0])
    idx = 1
    out = []
    
    for _ in range(T):
        M = int(data[idx])
        R = int(data[idx+1])
        idx += 2
        
        # K = (M^R - 1) / (M - 1) - R (mod MOD)
        m_pow_r = pow(M, R, MOD)
        geom_sum = (m_pow_r - 1) * pow(M - 1, MOD - 2, MOD) % MOD
        ans = (geom_sum - R) % MOD
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()