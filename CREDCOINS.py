# CRED Coins
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Basic Math

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        total_coins = x * y
        bags = total_coins // 100
        out.append(str(bags))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()