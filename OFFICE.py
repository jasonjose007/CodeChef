# Chef in his Office
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, 2 * t + 1, 2):
        x = int(data[i])
        y = int(data[i+1])
        # Chef works 4 days a week for X hours, and Friday for Y hours.
        total_hours = 4 * x + y
        results.append(str(total_hours))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()