# Count the Notebooks
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    results = []
    idx = 1
    for _ in range(T):
        N = int(input_data[idx])
        idx += 1
        # Each notebook costs 1000 grams of pulp, and 1 kg = 1000 grams.
        # N kg of pulp can make (N * 1000) / 1000 = N * 1000 / 1000 = N * 10 notebooks? 
        # Wait, 1 kg = 1000 grams. N kg = N * 1000 grams.
        # Each notebook uses 100 grams.
        # Total notebooks = (N * 1000) / 100 = N * 10.
        results.append(str(N * 10))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()