# Classic Vacuum Agent
# Includes




## Overview

- **Environment**: The agent is in a 5 x 5 2D Frontier Grid World.
- **Movement**: The agent can move in four directions: up, down, left, and right.
- **Sensing**: The agent can sense whether the square it is on is dirty and clean it.

## Assumptions

- The agent knows the layout of the grid world and the location of the dirty squares.
- The agent does not know the location of the starting square.

## Initialization

- The agent is initialized with a grid world, a starting node, and a heuristic function.

## Strategy

- **Algorithm**: We use A* search to find the optimal path to clean all the dirty squares.
  
### Priority Queue

- When selecting the next node to expand, we use a priority queue.
- **Priority**: f(n) = g(n) + h(n)
- The priority queue will always pop the node with the lowest `f(n)` value.

### Cost Function

- `g(n)`: The cost for each move and if the agent cleans a dirty square after moving to it.
  - Movement Cost = 1
  - Cleaning Cost = 1

### Heuristic Function

- `h(n)`: 
  - h(n) = distance to nearest dirty square
  - h2(n) = sum of distances to all dirty squares
  
#### Penalty

- Included in `h(n)` is the penalty for the remaining dirty squares.
  - Penalty = 2 * number of remaining dirty squares
  
### Goal State

- The goal state check passes if there are no more dirty squares in the grid world.

---

## Node Class

### Stores

- F(n) = g(n) + h(n) values
- Agent's current position (x, y)
- Agent's previous position (x, y)
- The nodes that are adjacent to the current node
- Starting node flag
- Flags for whether the node is dirty or clean
- Flags for whether the node is part of the optimal path

---

## Frontier Grid World

### Stores

- 2D array of nodes
- List of dirty nodes

### Checks

- If no more dirty nodes the goal state is reached
- If expanding a node will result in the agent moving out of bounds
- If a node is dirty or clean
- If a node is part of the optimal path
- If a node is the starting node

---

## Functions

### A* Search

- Returns the optimal path
- Returns the number of nodes expanded
- Returns the number of nodes in the optimal path
- Returns the total cost of the optimal path
- Cleans the dirty nodes in the optimal path

### Heuristic Function

- Returns the heuristic value of a node
- Returns the number of dirty nodes remaining
- Returns the distance from the current node to the nearest dirty node
