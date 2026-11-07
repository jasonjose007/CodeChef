# Passes for Fair
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
    out = []
    for i in range(1, 2 * t + 1, 2):
        n = int(data[i])
        k = int(data[i+1])
        if k > n:
            out.append("YES" if n + 1 >= k else "NO")
        else:
            out.append("YES" if k > n else "YES" if n + 1 >= k else "NO")
            
    for i in range(1, t + 1):
        n = int(data[2*i - 1])
        k = int(data[2*i])
        if k >= n + 1:
            out_str = "YES"
        else:
            out_str = "NO"
        out.append(out_str)
        
    # Correct logic for "Passes for Fair":
    # Chef has N friends, and Chef himself needs 1 pass. Total people = N + 1.
    # Chef has K passes. Chef can go to the fair with N friends if and only if K >= N + 1.
    
    results = []
    for i in range(1, len(data), 2):
        n = int(data[i])
        k = int(data[i+1])
        if k >= n + 1:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    main()