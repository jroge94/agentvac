import heapdict
from typing import Callable
from code.environment import *

def manhattan_distance(node: Node, grid: Grid) -> float:
    """
    Manhattan using sum of distances between all dirty nodes and the current node
    """
    return sum(abs(node.x - dirty_node.x) + abs(node.y - dirty_node.y) for dirty_node in grid.dirty_nodes)
    

##TODO: add more heuristics functions
##TODO: add a penalty for every dirty node left per step





## This is currently lacking the following features:
## - path cost
## - penalty cost for leaving a dirty node
def a_star_search(grid: Grid, heuristic: Callable[[Node, Grid], float]) -> tuple[set[Node], int, int, float]:
    
    
    start_node = grid.nodes[4][0] ## this should be moved to a function in the grid class and used in the main function
    start_node.g = 0
    start_node.h = heuristic(start_node, grid)
    start_node.f = start_node.g + start_node.h
    
    open_list = heapdict.heapdict()
    open_list[start_node] = start_node.f
    
    expanded_nodes = 0
    generated_nodes = 1
    
    with open('states.txt', 'w') as f:
        while open_list:
            
            current_node, _ = open_list.popitem()
            expanded_nodes += 1
            f.write(str(grid))
            f.write('\n\n')
            
            current_node.mark_visited() ## this can be deleted
            
            if current_node.is_dirty:
                grid.mark_clean(current_node.x, current_node.y)
                
                
            if grid.is_goal_reached():
                optimal_path = grid.reconstruct_path(current_node)
                path_cost = current_node.g
                
                
                return optimal_path, expanded_nodes, generated_nodes, path_cost

            neighbors = grid.get_neighbors(current_node)
            
            f.write(f'current_node -> {current_node.x}, {current_node.y} ->')
            f.write('\n')
                    
            for neighbor in neighbors:
                f.write(f'neighbor ->({neighbor.x}, {neighbor.y})->fvalue: {neighbor.f}')
                if neighbor.parent == current_node:
                    f.write('\n')
                    continue
        
        
                if neighbor.visited:
                    continue
                
        
                tentative_g = current_node.g + 1  
                
                if tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.h = heuristic(neighbor, grid)
                    
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current_node
                    generated_nodes += 1
                    open_list[neighbor] = neighbor.f
          
        return set(), expanded_nodes, generated_nodes, float('inf')
    
    