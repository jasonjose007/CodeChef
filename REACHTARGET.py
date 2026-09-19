# Reach the Target
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        idx += 2
        out.append(str(x - y))
    print('\n'.join(out))

if __name__ == '__main__':
    main()