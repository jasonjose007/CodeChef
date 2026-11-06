# Off By One
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = int(input_data[0])
    B = int(input_data[1])
    
    total = A + B
    # Print the sum followed by a '1'
    print(f"{total}1")

if __name__ == '__main__':
    main()