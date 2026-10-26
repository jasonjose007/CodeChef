# Cryptography
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    # The problem description and example format can be mapped to standard columnar transposition.
    # Looking at the example:
    # Keyword: ZEBRAS -> length 6.
    # Alphabetical order of letters in ZEBRAS ('A','B','E','R','S','Z'):
    # Z E B R A S
    # 6 3 2 4 1 5  (wait, Z is 6th, E is 3rd, B is 2nd, R is 4th, A is 1st, S is 5th alphabetically?
    # Let's check:
    # Z(6), E(3), B(2), R(4), A(1), S(5)
    # Sorted letters of ZEBRAS: A(1), B(2), E(3), R(4), S(5), Z(6)
    # Positions in original keyword:
    # A is at index 4 (0-based) -> 1st
    # B is at index 2 -> 2nd
    # E is at index 1 -> 3rd
    # R is at index 3 -> 4th
    # S is at index 5 -> 5th
    # Z is at index 0 -> 6th
    # So the order given in the example "6 3 2 4 1 5" corresponds to columns read order.
    # Wait, 6 3 2 4 1 5 means:
    # 1st column read is A (col 4)
    # 2nd column read is B (col 2)
    # 3rd column read is E (col 1)
    # 4th column read is R (col 3)
    # 5th column read is S (col 5)
    # 6th column read is Z (col 0)
    # The example output gives "EVLNE ACDTK ESEAQ ROFOJ DEECU WIREE".
    # Since this is a standard coding platform problem often matching a specific known template, 
    # let's write a robust parser that reads the permutation and the grid and outputs the ciphertext.

    # Actually, looking at typical CodeChef "Cryptography" problems with this exact text:
    # Input format:
    # Line 1: permutation or keyword? The example shows "6 3 2 4 1 5" as part of output description or input?
    # "Output Description \n 6 3 2 4 1 5 \n W E A R E D ... \n Output: EVLNE..."
    # Wait, usually the input contains the key/permutation and the grid, or we just need to implement Columnar Transposition.
    
    # Let's read all tokens.
    tokens = []
    for line in lines:
        tokens.extend(line.split())
        
    if not tokens:
        return

    # Let's parse the input assuming standard format where first few tokens might be the permutation, 
    # or the first line is the permutation numbers, followed by the grid characters.
    # In the example:
    # 6 3 2 4 1 5
    # W E A R E D I S C O V E R E D F L E E A T O N C E Q K J E U
    
    # Let's find where the integers representing the permutation are.
    perm = []
    idx = 0
    while idx < len(tokens) and tokens[idx].isdigit():
        perm.append(int(tokens[idx]))
        idx += 1
        
    if not perm:
        # Fallback if no leading numbers
        return

    k = len(perm)
    message_tokens = tokens[idx:]
    message = "".join(message_tokens) # or keep spaces? The example grid has spaces. 
    # Wait, the grid in the example has characters: W, E, A, R, E, D, ...
    # If we take all remaining tokens as characters of the grid row by row:
    
    grid = []
    current_row = []
    for token in message_tokens:
        current_row.append(token)
        if len(current_row) == k:
            grid.append(current_row)
            current_row = []
    if current_row:
        # pad if needed
        while len(current_row) < k:
            current_row.append('X')
        grid.append(current_row)
        
    # Now read column by column according to perm.
    # perm gives the 1-based index of columns to read.
    # e.g., 6 3 2 4 1 5 means read column 6, then 3, then 2, then 4, then 1, then 5 (0-indexed: 5, 2, 1, 3, 0, 4).
    
    cipher_words = []
    for p in perm:
        col_idx = p - 1
        col_chars = [row[col_idx] for row in grid if col_idx < len(row)]
        cipher_words.append("".join(col_chars))
        
    print(" ".join(cipher_words))

if __name__ == '__main__':
    solve()