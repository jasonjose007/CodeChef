# Just One More Episode
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys


def det_mod(mat, mod=1000000007):
    n = len(mat)
    if n == 0:
        return 1
    res = 1
    for i in range(n):
        pivot = -1
        for j in range(i, n):
            if mat[j][i] != 0:
                pivot = j
                break
        if pivot == -1:
            return 0
        if pivot != i:
            mat[i], mat[pivot] = mat[pivot], mat[i]
            res = (mod - res) % mod
        val = mat[i][i]
        res = (res * val) % mod
        inv = pow(val, mod - 2, mod)
        row_i = mat[i]
        for j in range(i + 1, n):
            if mat[j][i] != 0:
                factor = (mat[j][i] * inv) % mod
                row_j = mat[j]
                for k in range(i + 1, n):
                    row_j[k] = (row_j[k] - factor * row_i[k]) % mod
    return res


def count_spanning_trees(n, edges, mod=1000000007):
    if n <= 1:
        return 1
    if len(edges) < n - 1:
        return 0
    zero_indexed = any(u == 0 or v == 0 for u, v in edges)
    mat = [[0] * (n - 1) for _ in range(n - 1)]
    for u, v in edges:
        if not zero_indexed:
            u -= 1
            v -= 1
        if u == v:
            continue
        if u < n - 1:
            mat[u][u] = (mat[u][u] + 1) % mod
        if v < n - 1:
            mat[v][v] = (mat[v][v] + 1) % mod
        if u < n - 1 and v < n - 1:
            mat[u][v] = (mat[u][v] - 1) % mod
            mat[v][u] = (mat[v][u] - 1) % mod
    return det_mod(mat, mod)


def main():
    data = sys.stdin.read()
    if not data.strip():
        return
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    first_parts = lines[0].split()

    if len(first_parts) == 2:
        tokens = data.split()
        n = int(tokens[0])
        m = int(tokens[1])
        edges = []
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            idx += 2
            edges.append((u, v))
        print(count_spanning_trees(n, edges))
    elif len(first_parts) == 1:
        if len(lines) == 1:
            return
        second_parts = lines[1].split()
        tokens = data.split()
        if len(second_parts) == 2:
            t = int(tokens[0])
            idx = 1
            out = []
            for _ in range(t):
                n = int(tokens[idx])
                m = int(tokens[idx + 1])
                idx += 2
                edges = []
                for _ in range(m):
                    u = int(tokens[idx])
                    v = int(tokens[idx + 1])
                    idx += 2
                    edges.append((u, v))
                out.append(str(count_spanning_trees(n, edges)))
            print("\n".join(out))
        else:
            t = int(tokens[0])
            out = []
            for i in range(1, min(len(tokens), t + 1)):
                x = int(tokens[i])
                out.append("Yes" if x > 24 else "No")
            print("\n".join(out))


if __name__ == "__main__":
    main()