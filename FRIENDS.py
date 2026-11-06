# Friends
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    MOD = 10**9 + 7
    iterator = iter(input_data)
    
    t = int(next(iterator))
    
    out = []
    
    for _ in range(t):
        n = int(next(iterator))
        q = int(next(iterator))
        
        parent = list(range(n))
        size = [1] * n
        num_groups = n
        prod = 1
        
        def find(i):
            path = []
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for node in path:
                parent[node] = i
            return i

        def union(i, j):
            nonlocal num_groups, prod
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                # Update product by removing old sizes and multiplying new size
                # Since division by modulo is modular inverse, but wait:
                # prod is the product of sizes of *all* current roots.
                # When we merge root_i and root_j:
                # new_prod = (prod * inverse(size[root_i]) * inverse(size[root_j]) * (size[root_i] + size[root_j])) % MOD
                # But we can also just maintain it or compute it? Wait, q is up to 10^5, so O(1) per union is needed.
                # Let's use modular inverse.
                
                inv_i = pow(size[root_i], MOD - 2, MOD)
                inv_j = pow(size[root_j], MOD - 2, MOD)
                
                prod = (prod * inv_i) % MOD
                prod = (prod * inv_j) % MOD
                
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i
                    
                parent[root_j] = root_i
                size[root_i] += size[root_j]
                
                prod = (prod * size[root_i]) % MOD
                num_groups -= 1

        for _ in range(q):
            type_q = next(iterator)
            if type_q == '1':
                out.append(f"{num_groups} {prod}")
            else:
                x = int(next(iterator))
                y = int(next(iterator))
                union(x, y)
                
    print('\n'.join(out))

if __name__ == '__main__':
    solve()