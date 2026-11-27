# Course Registration
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts, Mathematics, Basic Math

import sys
input = sys.stdin.readline

def solve():
    line = input().strip()
    if not line:
        return
    t = int(line)
    out = []
    for _ in range(t):
        n, m, k = map(int, input().split())
        if n + k <= m:
            out.append("Yes")
        else:
            out.append("No")
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    solve()