# Reverse The Number
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Basic Math, Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        s = data[i]
        # Reverse the string representation of the number and convert back to int to remove leading zeros
        reversed_num = int(s[::-1])
        results.append(str(reversed_num))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()