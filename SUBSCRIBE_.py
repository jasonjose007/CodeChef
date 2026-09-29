# Subscriptions
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics, Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        m = int(data[idx])
        r = int(data[idx+1])
        idx += 2
        
        # The game with starting number M^R - 1, and modulo 10^9+7
        # Actually this is a placeholder solver since the problem statement template 
        # mixes TANDC and Subscriptions. Let's provide a robust handler.
        # Wait, the problem title in the text is "Subscriptions" (CodeChef SUBS).
        # Let's check SUBS problem: Chef wants to buy subscriptions for N friends.
        # Each subscription costs X rupees. Each subscription can be shared by 6 people.
        # Find minimum total cost.
        pass











def real_solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    out = []
    import math
    for i in range(1, T + 1):
        N = int(data[2*i - 1])
        X = int(data[2*i])
        subs = math.ceil(N / 6)
        out.append(str(subs * X))
    print('\n'.join(out))

real_solve()