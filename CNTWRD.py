# Counting Words
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    out = []
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        out.append(str(n * m))
        idx += 2

    print("\n".join(out))


if __name__ == "__main__":
    main()