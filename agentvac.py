from typing import List, Tuple, Dict, Set
import heapq

# --- Mocking Environment for standalone execution ---
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other): return False 
    def __eq__(self, other): return self.x == other.x and self.y == other.y
    def __hash__(self): return hash((self.x, self.y))
    def __repr__(self): return f"{self.x}, {self.y}"

class Grid:
    def __init__(self, rows, cols, dirty_nodes: Set[Tuple[int, int]]):
        self.rows = rows
        self.cols = cols
        self.dirty_nodes = set(dirty_nodes) # Make a copy to allow modification
    
    def get_neighbors(self, node: Node) -> List[Node]:
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = node.x + dx, node.y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                neighbors.append(Node(nx, ny))
        return neighbors

    def is_dirty(self, node: Node) -> bool:
        return (node.x, node.y) in self.dirty_nodes
    
    def clean(self, node: Node):
        if (node.x, node.y) in self.dirty_nodes:
            self.dirty_nodes.remove((node.x, node.y))

# --- Helper to match your Output Style ---
def print_env(grid: Grid, path_set: Set[Tuple[int,int]] = None):
    print("Current State of Environment")
    # Building a list of lists representation
    display_grid = [[' ' for _ in range(grid.cols)] for _ in range(grid.rows)]
    
    # Mark dirty nodes
    for r in range(grid.rows):
        for c in range(grid.cols):
            if (r, c) in grid.dirty_nodes:
                display_grid[r][c] = 'D'
            elif path_set and (r, c) in path_set:
                display_grid[r][c] = 'P'

    # Print in the style of list of lists (simplified numpy style)
    print("[", end="")
    for i, row in enumerate(display_grid):
        row_str = " ".join([f"'{c}'" for c in row])
        if i == 0:
            print(f"[{row_str}]")
        elif i == len(display_grid) - 1:
            print(f" [{row_str}]]")
        else:
            print(f" [{row_str}]")
    print() # Newline

def manhattan_distance(node: Node, goal: Node) -> float:
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def reconstruct_path(came_from: Dict[Node, Node], current: Node) -> List[Node]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# --- Main A* Function with Logging ---
def a_star_search(start: Node, goal: Node, grid: Grid, penalty_cost: int = 10):
    
    # Statistics trackers
    expanded_nodes_count = 0
    generated_nodes_count = 0
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from: Dict[Node, Node] = {}
    g_score: Dict[Node, float] = {start: 0}
    f_score: Dict[Node, float] = {start: manhattan_distance(start, goal)}
    
    visited = set()
    
    # Keep a copy of initial dirty nodes for final "Initial State" print
    initial_dirty_nodes = grid.dirty_nodes.copy()

    while open_set:
        # 1. Print Environment State
        print_env(grid)

        # 2. Pop Node
        current_f, current = heapq.heappop(open_set)
        
        if current in visited:
            continue
        visited.add(current)
        expanded_nodes_count += 1
        
        # 3. Print Current Node
        print(f"current_node -> {current.x}, {current.y} ->")
        

        # 4. Clean if dirty (based on your log where 'D's disappear)
        if grid.is_dirty(current):
            grid.clean(current)

        # Check Goal
        if current == goal:
            # Reconstruct Path
            path = reconstruct_path(came_from, current)
            path_set = {(n.x, n.y) for n in path}
            
            # --- Final Summary Output ---
            print("Initial State of Environment")
            # Temporarily restore dirty nodes to show initial state
            current_dirty = grid.dirty_nodes
            grid.dirty_nodes = initial_dirty_nodes
            print_env(grid)
            grid.dirty_nodes = current_dirty # Restore back
            
            print("Final State of Environment")
            print_env(grid, path_set) # Pass path_set to print 'P's
            
            print(f"expanded_nodes: {expanded_nodes_count}, generated_nodes: {generated_nodes_count}, path_cost: {int(g_score[current])}")
            return path

        # 5. Process Neighbors
        neighbors = grid.get_neighbors(current)
        neighbor_log_str = ""
        
        for neighbor in neighbors:
            generated_nodes_count += 1
            
            # Calculate costs
            move_cost = 1
            if grid.is_dirty(current):
                move_cost += penalty_cost
            
            tentative_g_score = g_score[current] + move_cost
            
            existing_f = f_score.get(neighbor, float('inf'))
            f_val_str = f"{existing_f}" if existing_f != float('inf') else "inf"
            neighbor_log_str += f"neighbor ->({neighbor.x}, {neighbor.y})->fvalue: {f_val_str}"

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        # Print gathered neighbor info
        print(neighbor_log_str)

    return []

if __name__ == "__main__":
    
    

    grid = Grid(5, 5, dirty_nodes={(0, 1)})
    
    start_node = Node(0, 0)
    goal_node = Node(4, 3)
    
    path = a_star_search(start_node, goal_node, grid, penalty_cost=10)
    
    print(f"Path found: {path}")
    
