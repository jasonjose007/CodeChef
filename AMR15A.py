# Mahasena
# Platform: CodeChef
# Difficulty: Easy
# Topics: Basic Programming Concepts, Mathematics

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    weapons = [int(x) for x in data[1:n+1]]
    
    lucky = sum(1 for w in weapons if w % 2 == 0)
    unlucky = n - lucky
    
    if lucky > unlucky:
        print("READY FOR BATTLE")
    else:
        print("NOT READY")

if __name__ == '__main__':
    main()