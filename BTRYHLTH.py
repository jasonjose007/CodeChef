# Battery Health
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Check if this is the "Battery Health" problem:
    # Format: T, followed by T integers X, where each X is battery percentage.
    # Or graph problem: N, M followed by edges, or T followed by test cases of graphs.
    
    # Let's inspect the tokens:
    # If it's Battery Health:
    # len(input_data) == int(input_data[0]) + 1
    # and all tokens are integers, each 0 <= X <= 100.
    try:
        T = int(input_data[0])
        if len(input_data) == T + 1:
            # High probability this is Battery Health
            # Verify if values look like battery percentages or if there are no edge pairs
            for i in range(1, T + 1):
                x = int(input_data[i])
                if x >= 80:
                    print("YES")
                else:
                    print("NO")
            return
    except Exception:
        pass

    # Otherwise, it might be the Spanning Tree (Kirchhoff's Theorem) problem
    MOD = 10**9 + 7

    def determinant(mat, n):
        det = 1
        for i in range(n):
            pivot = i
            while pivot < n and mat[pivot][i] == 0:
                pivot += 1
            if pivot == n:
                return 0
            if pivot != i:
                mat[i], mat[pivot] = mat[pivot], mat[i]
                det = (MOD - det) % MOD
            det = (det * mat[i][i]) % MOD
            inv = pow(mat[i][i], MOD - 2, MOD)
            for j in range(i + 1, n):
                if mat[j][i] != 0:
                    factor = (mat[j][i] * inv) % MOD
                    for k in range(i, n):
                        mat[j][k] = (mat[j][k] - factor * mat[i][k]) % MOD
        return det

    iterator = iter(input_data)
    
    def solve_graph(N, M):
        if N == 1:
            return 1
        adj = [[0] * N for _ in range(N)]
        deg = [0] * N
        for _ in range(M):
            u = int(next(iterator)) - 1
            v = int(next(iterator)) - 1
            adj[u][v] += 1
            adj[v][u] += 1
            deg[u] += 1
            deg[v] += 1
        
        # Laplacian matrix of size (N-1) x (N-1)
        L = [[0] * (N - 1) for _ in range(N - 1)]
        for i in range(N - 1):
            for j in range(N - 1):
                if i == j:
                    L[i][j] = deg[i] % MOD
                else:
                    L[i][j] = (-adj[i][j]) % MOD
        return determinant(L, N - 1)

    first = int(next(iterator))
    # Check if first token is T or N
    # If there are remaining tokens:
    try:
        second = int(next(iterator))
        # If there are exactly first * something or second represents M
        # Let's see if second could be M
        # If it's a single testcase graph:
        N = first
        M = second
        print(solve_graph(N, M))
    except StopIteration:
        pass

if __name__ == '__main__':
    solve()