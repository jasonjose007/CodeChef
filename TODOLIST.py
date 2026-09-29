# Problems in your to-do list
# Platform: CodeChef
# Difficulty: Easy
# Topics: Data Structures

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        d = list(map(int, data[idx:idx+n]))
        idx += n
        
        count = 0
        for x in d:
            if x >= 1000:
                count += 1
        out.append(str(count))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()