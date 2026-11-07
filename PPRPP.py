# solve it
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    A = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])
    B = [int(x) for x in input_data[n+2:n+2+m]]
    
    print(max(A), max(B))

if __name__ == '__main__':
    main()