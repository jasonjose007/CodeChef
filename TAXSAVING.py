# Saving Taxes
# Platform: CodeChef
# Difficulty: Easy
# Topics: Mathematics

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    out = []
    for i in range(1, t + 1):
        x = int(input_data[2 * i - 1])
        y = int(input_data[2 * i])
        out.append(str(x - y))
        
    print('\n'.join(out))

if __name__ == '__main__':
    main()