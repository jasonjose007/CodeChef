# Fitness
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        X = int(input_data[idx])
        idx += 1
        # Fitness problem on CodeChef: 
        # "Chef wants to calculate the total distance travelled in a week. 
        # He travels X km to office and back home each day, 5 days a week."
        # Wait, the problem description above was for TANDC, but the title says "Fitness".
        # Let's check standard CodeChef "Fitness": Chef goes to office and back home, so 2 * X per day, 5 days a week -> 10 * X.
        out.append(str(2 * 5 * X))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()