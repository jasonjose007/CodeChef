# First and Last Digit
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    for i in range(1, t + 1):
        s = input_data[i]
        first_digit = int(s[0])
        last_digit = int(s[-1])
        print(first_digit + last_digit)

if __name__ == '__main__':
    solve()