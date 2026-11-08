# Mad King
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
        
        adj = [[] for _ in range(n)]
        edges = []
        for _ in range(n - 1):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            idx += 2
            adj[u].append(v)
            adj[v].append(u)
            edges.append((u, v))
            
        troop_locs = []
        for _ in range(m):
            troop_locs.append(int(input_data[idx]))
            idx += 1
            
        if n == 1:
            out.append(f"{0.0:.6f}")
            continue
            
        # For a troop starting at u, the number of choices for new location is n - 1.
        # For an edge (u, v), removing it splits the tree into two components: S_u (containing u) and S_v (containing v).
        # A troop moves along the edge (u, v) if and only if its start location is in one component and its end location is in the other.
        # Specifically, if start is in S_u, end must be in S_v, and vice versa.
        
        # Let's compute sizes of components for each edge by rooting the tree at 0.
        parent = [0] * n
        depth = [0] * n
        size = [1] * n
        
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True
        
        # BFS/DFS to get tree structure
        stack = [0]
        order = []
        parent[0] = -1
        
        # iterative DFS
        q = [0]
        visited = [0] * n
        visited[0] = 1
        order = []
        
        # We can just use standard DFS to get subtree sizes
        def dfs(u, p):
            parent[u] = p
            size[u] = 1
            for v in adj[u]:
                if v != p:
                    dfs(v, u)
                    size[u] += size[v]
                    
        dfs(0, -1)
        
        # For each edge (u, v), one of them is the child of the other. Let's assume v is the child.
        # The subtree at v has size[v] nodes. The other component has n - size[v] nodes.
        # A troop at x choosing y uniformly at random from the other n-1 nodes:
        # Probability that a troop starting at i traverses edge (u, v):
        # - If i is in subtree of v (size[v] nodes):
        #   It must end up in the component of u (n - size[v] nodes).
        #   Since it cannot pick i itself, but i is in subtree of v, none of the target nodes in the other component are equal to i.
        #   So probability is (n - size[v]) / (n - 1).
        # - If i is NOT in subtree of v (n - size[v] nodes):
        #   It must end up in the subtree of v (size[v] nodes).
        #   If i is in the subtree of u, all size[v] nodes are valid, so probability is size[v] / (n - 1).
        #   If i IS i, wait. If i is u itself, u is not in subtree of v, and u is not in subtree of u. 
        #   Actually, let's be precise.
        #   For any starting node i:
        #   If i is in component A (size A), and edge connects A and B (size B = n - size A).
        #   If i is in A:
        #     Valid destinations are in B. Size of B is B. Total destinations = n - 1.
        #     Is i in B? No, i is in A. So all B destinations are valid.
        #     Prob = B / (n - 1).
        #   If i is in B:
        #     Valid destinations are in A. Size of A is A. Total destinations = n - 1.
        #     Is i in A? No, i is in B. So all A destinations are valid.
        #     Prob = A / (n - 1).
        #   Wait, this holds for ALL nodes i!
        #   If i is in A, it must go to B. Number of nodes in B is B. None of them is i. So prob is B / (n - 1).
        #   If i is in B, it must go to A. Number of nodes in A is A. None of them is i. So prob is A / (n - 1).
        #   So for a single troop, the probability of traversing edge (u, v) where v is child of u:
        #   - If troop starts in subtree(v): prob = (n - size[v]) / (n - 1)
        #   - If troop starts outside subtree(v): prob = size[v] / (n - 1)
        
        expected_lucky_roads = 0.0
        
        for u, v in edges:
            # identify which is child
            if parent[v] == u:
            # v is child of u
                sub_size = size[v]
            else:
                sub_size = size[u]
                
            # Count how many troops start in the subtree and how many outside
            # Actually, we can just check for each troop its probability
            prob_edge = 1.0
            for troop in troop_locs:
                # We need to know if troop is in the subtree of v (assuming v is child, or handle generally)
                # Let's root the edge check properly:
                # The two components are separated by removing (u, v).
                # Let's find which component contains each node by checking if node is in subtree of child.
                pass
            
        # Let's rewrite the edge traversal probability for a single troop for a specific edge (u, v):
        # Remove edge (u, v). The tree splits into two components. Let's find the component containing u (let's call it comp_u, size_u) and v (comp_v, size_v).
        # Wait, size of component containing v when edge (u,v) is removed is just size[v] if parent[v]==u else size[u].
        # Let's make a helper to check if node x is in the component of v when edge (u,v) is removed.
        # If parent[v] == u, the component containing v is the subtree of v. Size is size[v].
        # If parent[u] == v, the component containing u is the subtree of u. Size is size[u].
        
        total_lucky_roads = 0.0
        for u, v in edges:
            if parent[v] == u:
                child = v
            else:
                child = u
                
            sub_sz = size[child]
            other_sz = n - sub_sz
            
            # Count troops in subtree of child
            # A node x is in subtree of child if it's in child's component.
            # We can precalculate or just do a quick check. Since n <= 100, we can BFS/DFS or just check ancestor path.
            # Even simpler: root at 0. For edge (u, v) with parent[v] == u, subtree is v's subtree.
            # We can check if `t` is in subtree of `child`.
            
            # Let's write a function `in_subtree(node, root_of_subtree)`:
            # Actually, `node` is in subtree of `child` if `node == child` or `child` is an ancestor of `node`.
            # To check if `child` is ancestor of `node`: we can walk up from `node` using `parent`.
            
            def is_ancestor(anc, node):
                curr = node
                while curr != -1:
                    if curr == anc:
                        return True
                    curr = parent[curr]
                return False

            prob_all = 1.0
            for troop in troop_locs:
                in_sub = is_ancestor(child, troop)
                if in_sub:
                    p = other_sz / (n - 1)
                else:
                    p = sub_sz / (n - 1)
                prob_all *= p
                
            total_lucky_roads += prob_all
            
        out.append(f"{total_lucky_roads:.6f}")
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()