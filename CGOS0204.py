# Lazy Abhishek
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
        x = int(data[idx])
        y = int(data[idx+1])
        n = int(data[idx+2])
        idx += 3
        
        # Sum of first n multiples of x is x * (n * (n + 1)) // 2
        sum_x = x * n * (n + 1) // 2
        # Sum of first n multiples of y is y * (n * (n + 1)) // 2
        sum_y = y * n * (n + 1) // 2
        
        out.append(str(sum_x * sum_y))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()