import heapdict
from dataclasses import dataclass, field
from typing import Any, Callable, List
import numpy as np


@dataclass(order=True)
class Node:
    x: int
    y: int
    g: float = float('inf')
    h: float = float('inf')
    f: float = float('inf')
    is_path: bool = False
    is_start: bool = False
    is_dirty: bool = False
    visited: bool = False
    parent: Any = None
    neighbor: Any = None
    is_neighbor: bool = False
    actions: [] = field(default_factory=list)

    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __iter__(self):
        yield self.x
        yield self.y    
    
    def mark_path(self):
        self.is_path = True
        
    def mark_dirty(self):
        self.is_dirty = True
        
    def mark_clean(self):
        self.is_dirty = False
        self.actions.append("Clean")
        
    def mark_neighbor(self):
        self.is_neighbor = True
        
    def mark_visited(self):
        self.visited = True
        self.actions.append("Moved To")
    
@dataclass
class Grid:
    rows: int
    cols: int
    nodes: List[List[Node]] = field(init=False, default_factory=list)
    dirty_nodes: set[Node] = field(init=False, default_factory=set)
    optimal_path: set[Node] = field(init=False, default_factory=set)
    neighbors: set[Node] = field(init=False, default_factory=set)
    actions: set[Node] = field(init=False, default_factory=set)
    
    
    def __post_init__(self):
        self.grid = np.zeros((self.rows, self.cols), dtype=str)
        self.nodes = [[Node(x, y) for y in range(self.cols)] for x in range(self.rows)]
        self.dirty_nodes = set()
        self.optimal_path = set()
        self.actions = set()
        self.neighbors = set()
        

        
    def mark_dirty(self, x: int, y: int):
        self.nodes[x][y].mark_dirty()
        self.dirty_nodes.add(self.nodes[x][y])
        
    def mark_clean(self, x: int, y: int):
        self.nodes[x][y].mark_clean()
        self.dirty_nodes.remove(self.nodes[x][y])
        self.grid[x][y] = 'C'
        
    def mark_path(self, x: int, y: int):
        self.nodes[x][y].mark_path()
        self.optimal_path.add(self.nodes[x][y])
        
    def mark_visited(self, x: int, y: int):
        self.nodes[x][y].mark_visited()
        self.grid[x][y] = '*'
        
    
    def dirty_nodes_location(self) -> set[Node]:
        dirty_nodes_locs = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.nodes[i][j].is_dirty:
                    dirty_nodes_locs.append((i, j))
        return dirty_nodes_locs
    
    def get_neighbors_coords(self, node: Node) -> set:
        self.get_neighbors = set()
        for neighbor in self.get_neighbors(node):
            yield neighbor.x, neighbor.y, neighbor.f
            
        
    def get_neighbors(self, node: Node) -> set:
        neighbors = set()
        x, y = node.x, node.y
        if x > 0:
            neighbors.add(self.nodes[x - 1][y])
        if x < self.rows - 1:
            neighbors.add(self.nodes[x + 1][y])
        if y > 0:
            neighbors.add(self.nodes[x][y - 1])
        if y < self.cols - 1:
            neighbors.add(self.nodes[x][y + 1])
        return neighbors
    
    def is_goal_reached(self):
        return len(self.dirty_nodes) == 0
    
    def get_path(self):
        return self.optimal_path
    
    def is_on_optimal_path(self, node: Node):
        if node in self.optimal_path:
            return True
        return False
        
    
    def reconstruct_path(self, current_node: Node):
        path = set()
        while current_node is not None:
            path.add(current_node)
            current_node.mark_path()
            current_node = current_node.parent
        self.optimal_path = path
        
        return self.optimal_path
    
    def print_optimal_path(self):
        """
        Print the optimal path and the actions from start to goal.
        the fvalue of the nodes and the total heuristic value
        
        """
        print("\nOptimal Path:")
        
        for node in self.optimal_path:
            print(f"({node.x}, {node.y}) -> {node.actions} -> fvalue: {node.f}")
    
    def __str__(self):
        grid = np.zeros((self.rows, self.cols), dtype=str)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.nodes[i][j].is_path:
                    grid[i][j] = 'P'
                elif self.nodes[i][j].is_start:
                    grid[i][j] = 'S'
                elif self.nodes[i][j].is_dirty:
                    grid[i][j] = 'D'
                else:
                    grid[i][j] = ' '
        return '\n' + "Current State of Environment"+ '\n' + str(grid)