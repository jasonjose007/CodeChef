# Simple Sorting
# Platform: CodeChef
# Difficulty: Easy
# Topics: Data Structures, Queues, Algorithms

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    nums = [int(x) for x in input_data[1:t + 1]]
    nums.sort()
    sys.stdout.write('\n'.join(map(str, nums)) + '\n')

if __name__ == '__main__':
    main()