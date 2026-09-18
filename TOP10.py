# Masterchef finals
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

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
        if X <= 10:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()