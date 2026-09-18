# Reach on Time
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    out = []
    for i in range(1, T + 1):
        X = int(data[i])
        if X >= 30:
            out.append("YES")
        else:
            out.append("NO")
    print('\n'.join(out))

if __name__ == '__main__':
    main()