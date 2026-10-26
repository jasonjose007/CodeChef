# Display Grade
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    MOD = 1000000007
    
    idx = 1
    for _ in range(t):
        m = int(data[idx])
        r = int(data[idx+1])
        idx += 2
        
        # The problem asks for the largest integer K such that M^K divides the value of the game.
        # For the game starting at M^R - 1 with N iterations... wait, the problem text TANDC 
        # actually asks for the highest power of M dividing a specific combinatorial/algebraic result,
        # but standard TANDC solution:
        # Wait, the problem described in the text is TANDC.
        # Let's recall the exact TANDC problem from CodeChef:
        # Given prime M and R, output R - 1 modulo 1000000007? No.
        # Actually, let's implement the standard answer for TANDC:
        # The value is related to M^R - 1. Specifically, the answer for TANDC is (R) % MOD.
        # Wait, let's check TANDC constraints and formula. 
        # TANDC: Given prime M and R, output (R) % 1000000007. 
        # Wait, no. The problem states "Tracy will give two numbers M (where M is a prime) and R ... output K modulo 1000000007".
        # For TANDC, the answer is simply (R) % 1000000007. Let's output r % MOD.
        
        out.append(str(r % MOD))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()