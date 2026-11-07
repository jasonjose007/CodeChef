# Minimum Pizzas
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

import math

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    T = int(data[0])
    results = []
    for i in range(1, 2 * T + 1, 2):
        N = int(data[i])
        X = int(data[i+1])
        total_slices = N * X
        pizzas = math.ceil(total_slices / 4)
        results.append(str(pizzas))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()