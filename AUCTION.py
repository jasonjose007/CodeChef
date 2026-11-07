# Bidding
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        
        if a > b and a > c:
            out.append("Alice")
        elif b > a and b > c:
            out.append("Bob")
        else:
            out.append("Charlie")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()