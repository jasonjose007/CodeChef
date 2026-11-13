# Exams
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    out = []
    for i in range(1, T + 1):
        X = int(input_data[3*i - 2])
        Y = int(input_data[3*i - 1])
        Z = int(input_data[3*i])
        
        total_students = X * Y
        passing_students = Z
        
        if passing_students > total_students // 2:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()