# The Lead Game
# Platform: CodeChef
# Difficulty: Medium
# Topics: Data Structures, Arrays, Basic Programming Concepts, Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    
    max_lead = 0
    winner = 0
    
    p1_cum = 0
    p2_cum = 0
    
    idx = 1
    for _ in range(n):
        s1 = int(data[idx])
        s2 = int(data[idx+1])
        idx += 2
        
        p1_cum += s1
        p2_cum += s2
        
        if p1_cum > p2_cum:
            lead = p1_cum - p2_cum
            if lead > max_lead:
                max_lead = lead
                winner = 1
        else:
            lead = p2_cum - p1_cum
            if lead > max_lead:
                max_lead = lead
                winner = 2
                
    print(f"{winner} {max_lead}")

if __name__ == '__main__':
    solve()