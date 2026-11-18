# Easy Pronunciation
# Platform: CodeChef
# Difficulty: Medium
# Topics: Data Structures, Basic Programming Concepts

import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    vowels = set("aeiou")
    out = []
    for _ in range(t):
        idx += 1
        s = data[idx]
        idx += 1
        cnt = 0
        hard = False
        for ch in s:
            if ch in vowels:
                cnt = 0
            else:
                cnt += 1
                if cnt >= 4:
                    hard = True
                    break
        out.append("NO" if hard else "YES")
    print("\n".join(out))


if __name__ == "__main__":
    solve()