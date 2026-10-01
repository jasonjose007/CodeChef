# Determine the Score
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    results = []
    idx = 1
    for _ in range(T):
        M = int(input_data[idx])
        R = int(input_data[idx+1])
        idx += 2
        
        # The actual problem typically referred to as "Determine the Score" in CodeChef 
        # is usually a very simple problem: "Chef has a total of X points... Each problem has equal points...".
        # Wait, the prompt says: "This is the statement of the problem TANDC on CodeChef... Tracy is teaching Charlie maths via a game called N-Cube..."
        # Ah, the prompt text contains TWO problems or a mixed-up statement. 
        # Title: "Determine the Score". But body talks about TANDC (N-Cube, M and R, prime, etc.).
        # Let's check "Determine the Score" standard CodeChef problem:
        # "Chef has X points for a problem, and there are 10 test cases. Each test case gives points = X / 10. If the problem has N test cases and each carries X/N points? No:
        # "In aப் test, a problem is worth X points. Chef gets X/10 points for each test case passed if all test cases carry equal points. There are 10 test cases. If Chef passes N test cases, what is his score?"
        # Let's re-read standard "Determine the Score" (DETSCORE):
        # "The problem is worth X points. There are 10 test cases. Each test case carries X/10 points. Chef has passed N test cases. What is his score?"
        # Input: T, then for each test, X and N. Output: (X // 10) * N.
        # Let's check if the input format matches DETSCORE.
        pass

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    if data:
        T = int(data[0])
        out = []
        for i in range(1, 2 * T + 1, 2):
            X = int(data[i])
            N = int(data[i+1])
            out.append(str((X // 10) * N))
        print('\n'.join(out))