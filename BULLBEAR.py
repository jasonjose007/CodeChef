# Bull or Bear
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    out = []
    idx = 1
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        if y > x:
            out.append("PROFIT")
        elif y < x:
            out.append("LOSS")
        else:
            out.append("NEUTRAL")
            
    print('\n'.join(out))

if __name__ == '__main__':
    main()