# Map Sudoku
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    tokens = list(map(int, input_data))

    MOD = 10**9 + 7

    def count_spanning_trees(n, m, edges):
        if n == 1:
            return 1
        # Build Laplacian matrix of size (n-1) x (n-1)
        # Using 0-indexed vertices 0 to n-2
        deg = [0] * n
        adj = [[0] * n for _ in range(n)]

        for u, v in edges:
            u -= 1
            v -= 1
            if u != v:
                deg[u] += 1
                deg[v] += 1
                adj[u][v] += 1
                adj[v][u] += 1

        # Laplacian matrix size (n-1)
        k = n - 1
        mat = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if i == j:
                    mat[i][j] = (deg[i] - adj[i][j]) % MOD
                else:
                    mat[i][j] = (-adj[i][j]) % MOD

        # Determinant via Gaussian elimination
        det = 1
        for i in range(k):
            pivot = -1
            for r in range(i, k):
                if mat[r][i] % MOD != 0:
                    pivot = r
                    break
            if pivot == -1:
                return 0
            if pivot != i:
                mat[i], mat[pivot] = mat[pivot], mat[i]
                det = (MOD - det) % MOD

            det = (det * mat[i][i]) % MOD
            inv = pow(mat[i][i], MOD - 2, MOD)

            for r in range(i + 1, k):
                if mat[r][i] % MOD != 0:
                    factor = (mat[r][i] * inv) % MOD
                    for c in range(i, k):
                        mat[r][c] = (mat[r][c] - factor * mat[i][c]) % MOD

        return (det % MOD + MOD) % MOD

    # Check if first token is T
    # Each testcase has 2 + 2*M tokens (which is even).
    # If total length is odd, first token is T.
    if len(tokens) % 2 == 1:
        T = tokens[0]
        idx = 1
        for _ in range(T):
            if idx >= len(tokens):
                break
            n = tokens[idx]
            m = tokens[idx + 1]
            idx += 2
            edges = []
            for _ in range(m):
                u = tokens[idx]
                v = tokens[idx + 1]
                idx += 2
                edges.append((u, v))
            print(count_spanning_trees(n, m, edges))
    else:
        idx = 0
        while idx < len(tokens):
            n = tokens[idx]
            m = tokens[idx + 1]
            idx += 2
            edges = []
            for _ in range(m):
                u = tokens[idx]
                v = tokens[idx + 1]
                idx += 2
                edges.append((u, v))
            print(count_spanning_trees(n, m, edges))


if __name__ == "__main__":
    solve()