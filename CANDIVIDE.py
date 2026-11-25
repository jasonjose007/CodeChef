# Candy Division
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts, Mathematics

import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    results = []

    for i in range(1, T + 1):
        N = int(input_data[i])
        if N % 3 == 0:
            results.append("YES")
        else:
            results.append("NO")

    print("\n".join(results))


if __name__ == "__main__":
    main()