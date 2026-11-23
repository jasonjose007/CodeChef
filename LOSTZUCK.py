# Lost in a Grid
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys
from collections import deque


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1

    char_map = {
        '#': -1,
        '.': 0,
        '*': 0,
        'X': -2,
        'r': 1,
        'b': 2,
        'g': 4,
        'y': 8,
        'R': 17,
        'B': 18,
        'G': 20,
        'Y': 24,
    }

    out = []
    for _ in range(t):
        R = int(data[idx])

        C = int(data[idx + 1])
        idx += 2

        W = C + 2
        grid = [-1] * ((R + 2) * W)
        start_pos = -1

        for r in range(1, R + 1):
            row_str = data[idx]
            idx += 1
            base = r * W + 1
            for c, ch in enumerate(row_str):
                pos = base + c
                grid[pos] = char_map[ch]
                if ch == '*':
                    start_pos = pos

        visited = bytearray((R + 2) * W * 16)
        start_state = start_pos << 4
        visited[start_state] = 1
        q = deque([start_state])

        steps = 0
        found = -1
        dirs = (-W, W, -1, 1)

        while q and found == -1:
            for _ in range(len(q)):
                state = q.popleft()
                pos = state >> 4
                mask = state & 15

                for d in dirs:
                    npos = pos + d
                    val = grid[npos]
                    if val == -1:
                        continue
                    if val == -2:
                        found = steps + 1
                        break
                    if val == 0:
                        nmask = mask
                    elif val <= 8:
                        nmask = mask | val
                    else:
                        if not (mask & (val - 16)):
                            continue
                        nmask = mask

                    nstate = (npos << 4) | nmask
                    if not visited[nstate]:
                        visited[nstate] = 1
                        q.append(nstate)
                if found != -1:
                    break
            steps += 1

        if found != -1:
            out.append(str(found))
        else:
            out.append("Trapped!")

    print("\n".join(out))


if __name__ == "__main__":
    solve()