# Wordle
# Platform: CodeChef
# Difficulty: Easy
# Topics: Data Structures, Basic Programming Concepts

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        s = input_data[idx]
        g = input_data[idx+1]
        idx += 2
        
        res = []
        for i in range(5):
            if s[i] == g[i]:
                res.append('G')
            else:
                res.append('B')
        out.append("".join(res))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()