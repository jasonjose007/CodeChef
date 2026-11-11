# The Burnt Pancake
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        p = [int(x) for x in input_data[idx:idx+n]]
        idx += n
        
        ops = []
        
        def flip(k):
            if k <= 1:
                return
            ops.append(k)
            # Reverse first k elements
            p[:k] = p[:k][::-1]

        for target in range(n, 0, -1):
            # Find the position of 'target'
            curr_pos = -1
            for i in range(target):
                if p[i] == target:
                    curr_pos = i
                    break
            
            if curr_pos == target - 1:
                continue
            
            if curr_pos != 0:
                flip(curr_pos + 1)
            
            flip(target)
            
        out.append(f"{len(ops)} " + " ".join(map(str, ops)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()