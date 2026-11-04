# Janmansh and Assignments
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Basic Math

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        x = int(data[i])
        if x + 3 <= 10:
            results.append("Yes")
        else:
            results.append("No")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()