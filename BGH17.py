# BACTERIAL GROWTH
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        
        grid = []
        for _ in range(n):
            grid.append(list(input_data[idx]))
            idx += 1
            
        # A simple heuristic or fallback for small grids (n, m <= 10)
        # Since the problem allows up to 5000 moves and n, m <= 10,
        # we can use a general constructive strategy or BFS if needed,
        # but here we output a standard solution or -1 if impossible.
        # Given the complexity, let's implement a dummy valid solver that passes small cases
        # or matches the example if matched.
        
        # For the purpose of providing a complete structure:
        # We will output -1 if we can't easily solve, or a dummy sequence.
        # Wait, let's look at the example: 2 3 grid with one '.' at (2,3).
        # Actually, solving this generically for all T cases requires a full PEG solitaire style solver.
        # Since we must output valid moves, let's write a backtracking DFS / BFS to find the solution.
        
        start_cells = []
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '.':
                    start_cells.append((r+1, c+1))
        
        # If no start cell, -1
        if not start_cells:
            out.append("-1")
            continue
            
        # Attempt BFS/DFS to fill n*m - 1 cells
        target_empty = 1
        total_cells = n * m
        
        # State: tuple of cells containing organisms
        current_orgs = set(start_cells)
        
        # Due to time limits and complexity, let's use a BFS to find a path of length <= 5000
        from collections import deque
        
        queue = deque([(current_orgs, [])])
        visited_states = {frozenset(current_orgs)}
        
        found = False
        best_moves = []
        
        while queue:
            orgs, moves = queue.popleft()
            if len(orgs) == total_cells - target_empty:
                best_moves = moves
                found = True
                break
                
            if len(moves) >= 5000:
                continue
                
            # Generate next possible moves (Op 1 and Op 2)
            # Op 1: Move adjacent (r1, c1) -> (r2, c2) if (r2, c2) is empty
            # Op 2: Jump (r1, c1) -> (r3, c3) over (r2, c2) if (r1, c1) has org, (r2, c2) has org, (r3, c3) is empty
            
            org_list = list(orgs)
            # To speed up, we can limit branching or use heuristic
            for r1, c1 in org_list:
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    r2, c2 = r1 + dr, c1 + dc
                    if 1 <= r2 <= n and 1 <= c2 <= m:
                        if (r2, c2) not in orgs:
                            # Op 1
                            new_orgs = (orgs - {(r1, c1)}) | {(r2, c2)}
                            fs = frozenset(new_orgs)
                            if fs not in visited_states:
                                visited_states.add(fs)
                                queue.append((new_orgs, moves + [(r2, c2, r1, c1)]))
                        
                        # Op 2: jump
                        r3, c3 = r1 + 2*dr, c1 + 2*dc
                        if 1 <= r3 <= n and 1 <= c3 <= m:
                            if (r2, c2) in orgs and (r3, c3) not in orgs:
                                new_orgs = orgs | {(r3, c3), (r2, c2)} # wait, reproduction: middle gets child, organism jumps to empty non-middle
                                # "organism can jump to the empty non-middle cell while laying a child in the middle one"
                                # meaning: start at r1,c1. Jump to r3,c3. Middle r2,c2 gets a child.
                                # So r1,c1 stays or moves? "organism can jump" usually means it moves to r3,c3 and r2,c2 becomes filled.
                                # Let's check example: 2 1 2 3 (from 2,3 to 2,1? wait, example says: 2 1 2 3 -> from (2,3) to (2,1)?)
                                # Example: 2 1 2 3 means y2=2, x2=1, y1=2, x1=3 (using 1-based index y=row, x=col or vice versa? 
                                # Output format: y2, x2, y1, x1. In example: 2 1 2 3 -> (2,3) to (2,1) with middle (2,2).)
                                new_orgs = (orgs - {(r1, c1)}) | {(r3, c3), (r2, c2)}
                                fs = frozenset(new_orgs)
                                if fs not in visited_states:
                                    visited_states.add(fs)
                                    queue.append((new_orgs, moves + [(r3, c3, r1, c1)]))

        if found:
            out.append(str(len(best_moves)))
            for m_item in best_moves:
                out.append(f"{m_item[0]} {m_item[1]} {m_item[2]} {m_item[3]}")
        else:
            out.append("-1")

    print("\n".join(out))

if __name__ == '__main__':
    solve()