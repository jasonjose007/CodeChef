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
    
    max_lead_p1 = 0
    max_lead_p2 = 0
    
    c1 = 0
    c2 = 0
    
    idx = 1
    for _ in range(n):
        s1 = int(data[idx])
        s2 = int(data[idx+1])
        idx += 2
        
        c1 += s1
        c2 += s2
        
        if c1 > c2:
            lead = c1 - c2
            if lead > max_lead_p1:
                max_lead_p1 = lead
        else:
            lead = c2 - c1
            if lead > max_lead_p2:
                max_lead_p2 = lead
                
    if max_lead_p1 > max_lead_p2:
        print(f"1 {max_lead_p1}")
    else:
        print(f"2 {max_lead_p2}")

if __name__ == '__main__':
    solve()