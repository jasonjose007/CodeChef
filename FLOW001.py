# Add Two Numbers
# Platform: CodeChef
# Difficulty: Easy
# Topics: Algorithms

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    out = []
    for _ in range(T):
        A = int(input_data[idx])
        B = int(input_data[idx+1])
        idx += 2
        out.append(str(A + B))
        
    print('\n'.join(out))

if __name__ == '__main__':
    main()