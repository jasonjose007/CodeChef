# Second Largest
# Platform: CodeChef
# Difficulty: Easy
# Topics: Special, Basic Programming Concepts, Mathematics

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    out = []
    for _ in range(T):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        if (a > b) != (a > c):
            out.append(str(a))
        elif (b > a) != (b > c):
            out.append(str(b))
        else:
            out.append(str(c))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()