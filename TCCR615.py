# Freshers Task
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import bisect
import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    T = int(next(iterator))
    for _ in range(T):
        N = int(next(iterator))
        M = int(next(iterator))
        students = []
        for _ in range(M):
            a = int(next(iterator))
            b = int(next(iterator))
            if a > b:
                a, b = b, a
            students.append((a, b))

        students.sort(key=lambda x: (x[0], x[1]))

        tails = []
        for a, b in students:
            idx = bisect.bisect_left(tails, b)
            if idx == len(tails):
                tails.append(b)
            else:
                tails[idx] = b

        print(len(tails))


if __name__ == "__main__":
    main()