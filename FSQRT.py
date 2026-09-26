# Finding Square Roots
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts

import sys
import math

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    results = []
    for i in range(1, T + 1):
        n = int(input_data[i])
        results.append(str(math.isqrt(n)))
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    main()