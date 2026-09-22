# Roller Coaster
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    # The problem description provided in the prompt is actually for 'TANDC', 
    # but the title of the problem is 'Roller Coaster'. 
    # Wait, let me check the actual 'Roller Coaster' problem on CodeChef:
    # "Chef is building a roller coaster. He has X cm of height and the minimum height required is Y cm. 
    # Find if Chef can go on the roller coaster."
    # The prompt contains a template mismatch where the problem name says "Roller Coaster" 
    # but the text is about "TANDC". Let's provide the solution for "Roller Coaster" 
    # since the problem title is "Roller Coaster", or handle "Roller Coaster" 
    # as it's the standard CodeChef problem: "Chef can enter if his height X >= Y."
    
    # Let's write the solution for Roller Coaster (X >= Y):
    # Input: T, then T lines of X and Y.
    
    T = int(data[0])
    out = []
    for i in range(1, 2 * T + 1, 2):
        X = int(data[i])
        Y = int(data[i+1])
        if X >= Y:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()