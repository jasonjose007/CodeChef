# Problem 7
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        A = int(data[idx])
        B = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        
        N = A + B
        
        if K == 0:
            if A == 0:
                out.append(0)
            else:
                out.append(-1)
            continue
            
        ans = -1
        # We can iterate over the number of zeros we choose to flip, let's say `i` zeros and `K - i` ones.
        # Let current zeros be z and ones be o.
        # In one move, if we pick `i` zeros and `K - i` ones:
        # new_z = z - i + (K - i) = z + K - 2i
        # new_o = o - (K - i) + i = o - K + 2i
        # Constraints on i:
        # 0 <= i <= z (can't flip more zeros than available)
        # 0 <= K - i <= o (can't flip more ones than available) => K - o <= i <= K
        # So max(0, K - o) <= i <= min(z, K)
        # Also i must have the same parity constraints? No, any i in range is valid transition.
        # Since N <= something? Wait, what are the constraints on A, B, K? 
        # The problem description doesn't explicitly state the max value of A, B, K, but usually N can be up to 10^5 or similar. 
        # Wait, if N is large, BFS might be too slow. Let's analyze if BFS on `z` (number of zeros) is sufficient.
        # z ranges from 0 to N, so there are N+1 states. N could be large? 
        # Wait, if N is up to 10^5, BFS takes O(N * K) or O(N) if we optimize. But wait, what is the max N? 
        # Usually these problems have N <= 2000 or similar for O(N^2) or BFS. 
        # Let's check typical constraints for this problem. Often N <= 2000.
        
        # Let's write a BFS queue. Since N might be up to 2000 or so, let's use BFS.
        from collections import deque
        
        dist = [-1] * (N + 1)
        queue = deque([A])
        dist[A] = 0
        
        possible = False
        while queue:
            z = queue.popleft()
            o = N - z
            if z == 0:
                ans = dist[z]
                possible = True
                break
                
            min_i = max(0, K - o)
            max_i = min(z, K)
            
            for i in range(min_i, max_i + 1):
                nz = z + K - 2 * i
                if 0 <= nz <= N and dist[nz] == -1:
                    dist[nz] = dist[z] + 1
                    queue.append(nz)
                    
        out.append(ans)
        
    print('\n'.join(map(str, out)))

if __name__ == '__main__':
    solve()