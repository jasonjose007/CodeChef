# Ageing
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        X = int(data[i])
        results.append(str(X - 10))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()