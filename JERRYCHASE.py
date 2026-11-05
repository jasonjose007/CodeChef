# Tom and Jerry Chase
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        x = int(data[i])
        # Tom's speed is X, Jerry's speed is Y = 1 (implied: "Tom can catch Jerry if Tom's speed > Jerry's speed")
        # Wait, the standard problem: Tom has speed X, Jerry has speed Y. Usually Y=1 or given. 
        # Wait, the problem name is "Tom and Jerry Chase". Let's check standard constraints.
        # Usually: Tom's speed is X, Jerry's speed is Y. If X > Y, Tom catches Jerry.
        # But here only X is given? Wait, let's re-read standard "Tom and Jerry Chase" on CodeChef:
        # "Tom's speed is X, Jerry's speed is Y. Can Tom catch Jerry?" -> Wait, usually it's X < Y means Tom can't, X > Y means Tom can? 
        # Actually, in "Tom and Jerry Chase" (TANDJ): Tom runs at speed X, Jerry at speed Y. Wait, if Tom's speed is strictly greater than Jerry's speed, Tom can catch Jerry. But the input usually has X and Y? 
        # Ah, looking at the standard problem "Tom and Jerry Chase" (TANDJ): 
        # "Tom has speed X and Jerry has speed Y." - wait, the problem statement text above is just a dummy example markdown, but the problem title is "Tom and Jerry Chase".
        # Let's check standard TANDJ problem: X and Y are given. Wait, if only X is given in the snippet? No, let's read standard TANDJ: "Chef has X and Y...". 
        # Wait, if input has X, Y:
        # Let's write a robust parser just in case: if two integers per test case X and Y.
        pass













def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        if x < y:
            out.append("YES")
        else:
            out.append("NO")
    print('\n'.join(out))

if __name__ == '__main__':
    main()