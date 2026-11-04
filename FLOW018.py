# Small Factorial
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts, Mathematics, Basic Math, Algorithms, CPP

import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(input_data[i])
        results.append(str(math.factorial(N)))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()