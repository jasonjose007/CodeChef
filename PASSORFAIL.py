# Pass or Fail
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts, Mathematics, Algorithms

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    T = int(data[0])
    results = []
    
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        X = int(data[idx+1])
        P = int(data[idx+2])
        idx += 3
        
        correct_marks = X * 3
        incorrect_marks = (N - X) * (-1)
        total_score = correct_marks + incorrect_marks
        
        if total_score >= P:
            results.append("PASS")
        else:
            results.append("FAIL")
            
    print('\n'.join(results))

if __name__ == '__main__':
    main()