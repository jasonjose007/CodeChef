# Chef And Operators
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
    idx = 1
    out = []
    
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        
        if a > b:
            out.append('>')
        elif a < b:
            out.append('<')
        else:
            out.append('=')
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()