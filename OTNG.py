# Outing - Plan
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    num_test_cases = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(num_test_cases):
        if idx >= len(input_data):
            break
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        
        if n > k:
            out.append("1/1")
        elif n == 0:
            out.append("0/1")
        else:
            total = k ** n
            valid = (k + 1 - n) * ((k + 1) ** (n - 1))
            thrown = total - valid
            g = math.gcd(thrown, total)
            out.append(f"{thrown // g}/{total // g}")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()