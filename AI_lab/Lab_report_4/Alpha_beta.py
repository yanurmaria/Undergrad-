import random
import math

def execute_minimax(depth, node_idx, is_max, tree, limit, telemetry):
    telemetry['mm_count'] += 1
    if depth == limit:
        return tree[node_idx]
        
    left_child = node_idx * 2
    right_child = left_child + 1
    
    if is_max:
        return max(execute_minimax(depth + 1, left_child, False, tree, limit, telemetry),
                   execute_minimax(depth + 1, right_child, False, tree, limit, telemetry))
    else:
        return min(execute_minimax(depth + 1, left_child, True, tree, limit, telemetry),
                   execute_minimax(depth + 1, right_child, True, tree, limit, telemetry))

def execute_pruning(depth, node_idx, is_max, tree, limit, a, b, telemetry):
    telemetry['ab_count'] += 1
    if depth == limit:
        return tree[node_idx]
        
    left_child = node_idx * 2
    right_child = left_child + 1
    
    if is_max:
        v = float('-inf')
        v = max(v, execute_pruning(depth + 1, left_child, False, tree, limit, a, b, telemetry))
        a = max(a, v)
        if b <= a:
            return v
        v = max(v, execute_pruning(depth + 1, right_child, False, tree, limit, a, b, telemetry))
        return v
    else:
        v = float('inf')
        v = min(v, execute_pruning(depth + 1, left_child, True, tree, limit, a, b, telemetry))
        b = min(b, v)
        if b <= a:
            return v
        v = min(v, execute_pruning(depth + 1, right_child, True, tree, limit, a, b, telemetry))
        return v

if __name__ == "__main__":
    game_tree = [random.randint(2, 25) for _ in range(8)]
    max_d = int(math.log2(len(game_tree)))
    stats = {'mm_count': 0, 'ab_count': 0}
    
    print(f"Generated Leaf Nodes: {game_tree}")
    
    optimal = execute_minimax(0, 0, True, game_tree, max_d, stats)
    print("Minimax:")
    print(f"  Nodes Evaluated: {stats['mm_count']}")
    print(f"  Optimal Value: {optimal}")
    
    execute_pruning(0, 0, True, game_tree, max_d, float('-inf'), float('inf'), stats)
    
    nodes_saved = stats['mm_count'] - stats['ab_count']
    yield_pct = (nodes_saved / stats['mm_count']) * 100
    
    print("Alpha-Beta Pruning:")
    print(f"  Nodes Evaluated: {stats['ab_count']}")
    print(f"  Nodes Pruned: {nodes_saved}")
    print(f"Efficiency Improvement: {yield_pct:.2f}%")
