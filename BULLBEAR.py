# Bull or Bear
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, 2 * t + 1, 2):
        x = int(data[i])
        y = int(data[i+1])
        if y > x:
            out.append("PROFIT")
        elif y < x:
            out.append("LOSS")
        else:
            out.append("NEUTRAL")
    print('\n'.join(out))

if __name__ == '__main__':
    main()