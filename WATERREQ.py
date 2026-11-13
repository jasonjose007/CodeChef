# Water Requirement
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        out.append(str(2 * n))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()