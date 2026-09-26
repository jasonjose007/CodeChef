# Sum of Digits
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Algorithms

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        s = input_data[i]
        results.append(str(sum(ord(c) - 48 for c in s)))
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    main()