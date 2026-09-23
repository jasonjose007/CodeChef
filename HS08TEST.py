# ATM
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    x = int(input_data[0])
    y = float(input_data[1])
    
    if x % 5 == 0 and x + 0.50 <= y:
        y -= x + 0.50
        
    print(f"{y:.2f}")

if __name__ == '__main__':
    main()