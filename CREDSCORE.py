# Credit score
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def solve():
    # Read the single integer credit score
    line = sys.stdin.readline()
    if not line:
        return
    X = int(line.strip())
    
    # Problem: Credit score - Check if credit score is 750 or more
    if X >= 750:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()