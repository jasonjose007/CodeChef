# COLLECTER
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        idx += 2
        
        a = []
        for _ in range(n):
            a.append(int(input_data[idx]))
            idx += 1
            
        dp = [False] * (k + 1)
        dp[0] = True
        
        for x in a:
            if x > k:
                continue
            for j in range(x, k + 1):
                if dp[j - x]:
                    dp[j] = True
                    
        ans = 0
        for j in range(k, -1, -1):
            if dp[j]:
                ans = j
                break
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()