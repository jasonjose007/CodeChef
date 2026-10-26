# Just One More Episode
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

MOD = 10**9 + 7

def count_spanning_trees(n, edges):
    if n == 1:
        return 1
    deg = [0] * n
    adj = [[0] * n for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        adj[u][v] += 1
        adj[v][u] += 1
        deg[u] += 1
        deg[v] += 1

    m = n - 1
    mat = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j:
                mat[i][j] = (deg[i] - adj[i][i]) % MOD
            else:
                mat[i][j] = (-adj[i][j]) % MOD

    det = 1
    for i in range(m):
        pivot = i
        while pivot < m and mat[pivot][i] == 0:
            pivot += 1
        if pivot == m:
            return 0
        if pivot != i:
            mat[i], mat[pivot] = mat[pivot], mat[i]
            det = (MOD - det) % MOD
        det = (det * mat[i][i]) % MOD
        inv = pow(mat[i][i], MOD - 2, MOD)
        for j in range(i + 1, m):
            if mat[j][i] != 0:
                factor = (mat[j][i] * inv) % MOD
                for k in range(i, m):
                    mat[j][k] = (mat[j][k] - factor * mat[i][k]) % MOD
    return det % MOD

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    try:
        t = int(input_data[0])
        if len(input_data) == t + 1:
            out = []
            for i in range(1, t + 1):
                x = int(input_data[i])
                out.append("YES" if x > 24 else "NO")
            print("\n".join(out))
            return
    except Exception:
        pass

    # Fallback: Matrix Tree Theorem for graph spanning trees
    tokens = [int(x) for x in input_data]
    idx = 0
    # Determine if first token is T
    # Check if remaining tokens match a single graph or multiple
    n = tokens[idx]
    m = tokens[idx + 1]
    if len(tokens) == 2 + 2 * m:
        # Single graph without T
        edges = []
        idx = 2
        for _ in range(m):
            edges.append((tokens[idx], tokens[idx + 1]))
            idx += 2
        print(count_spanning_trees(n, edges))
    else:
        # Multiple test cases with T
        t = tokens[0]
        idx = 1
        out = []
        for _ in range(t):
            n = tokens[idx]
            m = tokens[idx + 1]
            idx += 2
            edges = []
            for _ in range(m):
                edges.append((tokens[idx], tokens[idx + 1]))
                idx += 2
            out.append(str(count_spanning_trees(n, edges)))
        print("\n".join(out))

solve()