# Burgers
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    out = []
    idx = 1
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        idx += 2
        out.append(str(min(a, b)))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()