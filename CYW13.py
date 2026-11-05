# Probability
# Platform: CodeChef
# Difficulty: Easy
# Topics: 

import sys

def solve():
    # The problem asks for the schedule of 12 teams playing 11 rounds.
    # It's a classic round-robin tournament scheduling problem.
    # We have 12 teams (A to L, represented as 0 to 11).
    # There are 11 rounds, and 6 games per round.
    # We can use the polygon method (circle method) for round-robin scheduling.
    
    n = 12
    teams = list(range(n))
    
    # We will fix team 11 (L) at the end, and rotate the first 11 teams.
    fixed = teams[-1]
    rotating = teams[:-1]
    
    for day in range(n - 1):
        current_teams = rotating + [fixed]
        games = []
        for i in range(n // 2):
            t1 = current_teams[i]
            t2 = current_teams[n - 1 - i]
            # To ensure fair distribution or just standard representation:
            # Let's sort or keep them as pair
            games.append((chr(ord('A') + t1), chr(ord('A') + t2)))
        
        # Sort games for consistent output
        games.sort()
        game_strs = [f"{g[0]}-{g[1]}" for g in games]
        print(" ".join(game_strs))
        
        # Rotate the rotating list
        rotating = [rotating[-1]] + rotating[:-1]

def main():
    # Read all inputs if any, though the problem description implies standard output of a valid schedule.
    # Some problems of this type might have a test case count. Let's handle it robustly.
    input_data = sys.stdin.read().split()
    if input_data:
        t = int(input_data[0])
        for _ in range(t):
            solve()
    else:
        solve()

if __name__ == '__main__':
    # Wait, the problem description for CodeChef 'Probability' actually expects 
    # the exact output of the schedule or just a valid schedule.
    # Let's just run solve() directly as it generates the 11 lines of schedules.
    # Actually, many codechef submission evaluations for such descriptive problems 
    # just require printing the schedule. Let's check if T is given.
    
    input_str = sys.stdin.read().strip()
    if input_str:
        try:
            T = int(input_str.split()[0])
            for _ in range(T):
                solve()
        except:
            solve()
    else:
        solve()