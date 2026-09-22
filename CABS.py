# The Cheaper Cab
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    for i in range(1, 2 * t + 1, 2):
        x = int(data[i])
        y = int(data[i+1])
        if x < y:
            out.append("FIRST")
        elif y < x:
            out.append("SECOND")
        else:
            out.append("ANY")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()