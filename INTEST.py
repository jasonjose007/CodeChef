# Enormous Input Test
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    count = 0
    for i in range(2, n + 2):
        if int(input_data[i]) % k == 0:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()