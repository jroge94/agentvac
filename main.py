import heapdict
from code.agentvac import a_star_search, manhattan_distance
from code.environment import *


    
grid = Grid(5, 5)
    
grid.mark_dirty(0, 0)
grid.mark_dirty(0, 1)
grid.mark_dirty(0, 2)
grid.mark_dirty(0, 3)
grid.mark_dirty(0, 4)

with open('states.txt', 'a') as f:
    f.write(f'Initial State of Environment')
    f.write(str(grid))
    _, expanded_nodes, generated_nodes, path_cost = a_star_search(grid, manhattan_distance)
    f.write('\n\n')
    f.write(f'Final State of Environment')
    f.write(str(grid))
    
    f.write(f'\nexpanded_nodes: {expanded_nodes}, generated_nodes: {generated_nodes}, path_cost: {path_cost}')
    #print(f'expanded_nodes: {expanded_nodes}, generated_nodes: {generated_nodes}, path_cost: {path_cost}') 
    
    f.write('\n')
    f.write(str(grid.print_optimal_path()))
    
    f.close()