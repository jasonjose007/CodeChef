# Six Friends
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Algorithms, Constructive

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    out = []
    idx = 1
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        cost_double = 3 * x
        cost_triple = 2 * y
        
        out.append(str(min(cost_double, cost_triple)))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()