# Python AI Project: 5x5 Frontier Grid World Agent

## Overview

- **Environment**: A 5 x 5 2D Frontier Grid World.
- **Movement**: The agent can move up, down, left, or right.
- **Sensing**: The agent detects if its current square is dirty and can clean it.

## Assumptions

- The agent is aware of the grid layout and the locations of dirty squares.
- The starting position of the agent is unknown to it.

## Initialization

- Initialization involves setting up the grid world, defining the starting node, and providing a heuristic function.

## Strategy

- **Algorithm Used**: A* Search Algorithm

### Priority Queue

- A priority queue is used to determine the next node to expand.
- **Priority Calculation**: f(n) = g(n) + h(n), where nodes with the lowest `f(n)` value are prioritized.

### Cost Function

- `g(n)`: Represents the movement cost (1) and additional cleaning cost (1) if the agent cleans a dirty square.

### Heuristic Function

- `h(n)`: The sum of distances to all remaining dirty squares.

### Goal State

- The goal is achieved when no dirty squares remain in the grid world.

## Frontier Grid World Details

### Data Storage

- The grid is represented as a 2D array of nodes.
- Maintains a list of dirty nodes.

### Key Checks

- Determines if the goal state (no dirty nodes) is reached.
- Ensures movements do not take the agent out of bounds.
- Checks whether nodes are dirty or clean.
- Identifies nodes that are part of the optimal path.
- Identifies the starting node.

---

## Key Functions

### A* Search

- Finds and returns the optimal path.
- Counts and returns the number of nodes expanded.
- Determines the number of nodes in the optimal path.
- Calculates the total cost of the optimal path.
- Cleans dirty nodes along the optimal path.

### Heuristic Function

- Provides the heuristic value for a given node.
- Counts and returns the number of dirty nodes remaining.
- Calculates the distance from the current node to the nearest dirty node.

---
