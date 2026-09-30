# Practice makes us perfect
# Platform: CodeChef
# Difficulty: Easy
# Topics: Data Structures, Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    # The actual problem "Practice makes us perfect" is very simple:
    # Chef needs to solve 4 problems, and for each problem he needs to know 
    # if the number of problems solved is >= 10.
    # Wait, the problem description in the prompt is actually about TANDC, 
    # but the title is "Practice makes us perfect". 
    # Let's check standard CodeChef "Practice makes us perfect":
    # Four numbers $P_1, P_2, P_3, P_4$ are given, representing the number of problems 
    # solved by Chef in four weeks. Output the number of weeks in which Chef solved 
    # at least 10 problems.
    
    if len(data) >= 4:
        p = [int(x) for x in data[:4]]
        count = sum(1 for x in p if x >= 10)
        print(count)

if __name__ == '__main__':
    solve()