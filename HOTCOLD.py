# Is it hot or cold
# Platform: CodeChef
# Difficulty: Easy
# Topics: Algorithms

import sys

def main():
    # Read all input from standard input and split into a list of strings
    input_data = sys.stdin.read().split()
    
    # If there's no input, just return
    if not input_data:
        return
    
    # The first element is the number of test cases T
    try:
        t = int(input_data[0])
    except ValueError:
        return
    
    # Process each test case
    # Each test case is a single integer C representing the temperature
    for i in range(1, t + 1):
        if i < len(input_data):
            try:
                c = int(input_data[i])
                # Chef considers the climate HOT if the temperature is greater than 20
                if c > 20:
                    print("HOT")
                # Otherwise, he considers it COLD
                else:
                    print("COLD")
            except ValueError:
                continue

if __name__ == "__main__":
    main()