# IPL Ticket Rush
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, 2 * t + 1, 2):
        n = int(data[i])
        m = int(data[i+1])
        if n > m:
            results.append(str(n - m))
        else:
            results.append("0")
            
    print('\n'.join(results))

if __name__ == '__main__':
    main()