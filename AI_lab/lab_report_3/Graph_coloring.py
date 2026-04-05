import sys

def is_safe(v, graph, color_assignment, c):
    """Check if the color c is safe for vertex v."""
    for neighbor in graph[v]:
        if color_assignment[neighbor] == c:
            return False
    return True

def solve_coloring(v, n, k, graph, color_assignment):
    """Recursive backtracking function to color the graph."""
    if v == n:
        return True

    for c in range(1, k + 1):
        if is_safe(v, graph, color_assignment, c):
            color_assignment[v] = c
            if solve_coloring(v + 1, n, k, graph, color_assignment):
                return True
            # Backtrack
            color_assignment[v] = 0
            
    return False

def main():
    try:
        with open("input.txt", "r") as f:
            lines = f.readlines()
            if not lines: return
            
            # Read N, M, K
            n, m, k = map(int, lines[0].split())
            graph = [[] for _ in range(n)]
            
            # Read M edges
            for i in range(1, m + 1):
                u, v = map(int, lines[i].split())
                graph[u].append(v)
                graph[v].append(u)

        color_assignment = [0] * n
        
        if solve_coloring(0, n, k, graph, color_assignment):
            print(f"Coloring Possible with {k} Colors")
            print(f"Color Assignment: {color_assignment}")
        else:
            print(f"Coloring Not Possible with {k} Colors")
            
    except FileNotFoundError:
        print("Error: input.txt not found.")

if __name__ == "__main__":
    main()
