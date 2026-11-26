# Candies
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    MAX_N = 100
    ans = [[0.0] * (MAX_N + 1) for _ in range(MAX_N + 1)]
    
    pow2 = [0.5**i for i in range(MAX_N + 5)]
    
    dp = {(0, 1): 1.0}
    
    for step in range(1, MAX_N + 1):
        next_dp = {}
        for (k, l), p in dp.items():
            p_same = pow2[l]
            p_inc = 1.0 - p_same
            
            # inc
            st1 = (k + 1, 1)
            next_dp[st1] = next_dp.get(st1, 0.0) + p * p_inc
            
            # same
            st2 = (k, l + 1)
            next_dp[st2] = next_dp.get(st2, 0.0) + p * p_same
            
        dp = next_dp
        for (k, l), p in dp.items():
            if k <= MAX_N:
                ans[step][k] += p

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    out = []
    for _ in range(T):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        
        if k > n or k < 0:
            res = 0.0
        else:
            res = ans[n][k]
        out.append(f"{res:.9f}")
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()