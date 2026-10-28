# Donation Drive
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    results = []
    for i in range(1, T + 1):
        N = int(input_data[2 * i - 1])
        X = int(input_data[2 * i])
        results.append(str(N - X))
        
    print('\n'.join(results))

if __name__ == '__main__':
    main()