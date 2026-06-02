# Python AI Project: 5x5 Frontier Grid World Agent

## 1. Overview

This project implements an intelligent agent navigating a **5x5 Frontier Grid World**.

* **Environment**: A discrete 5x5 2D grid.
* **Movement**: The agent can move `UP`, `DOWN`, `LEFT`, or `RIGHT`.
* **Sensing**: The agent detects if its current square is **dirty** and automatically cleans it.

## 2. Assumptions

1. **Full Observability**: The agent knows the grid layout and the precise locations of all dirty squares.
2. **Unknown Start**: The agent's specific starting coordinate is initially unknown to the logic (it must be provided or discovered at runtime).

## 3. Initialization

Initialization involves three key steps:

1. Setting up the `GridWorld` environment.
2. Defining the **Starting Node**.
3. Injecting the **Heuristic Function** logic.

---

## 4. Strategy: A* Search Algorithm

The core intelligence is powered by the **A* Search Algorithm**.

###  Priority Queue

A min-priority queue determines the next node to expand to ensure optimality.

* **Priority Calculation**:



*Nodes with the lowest  are expanded first.*

### Cost Function ()

The cost to reach a node includes movement and action costs:

* **Movement**: +1 per step.
* **Cleaning**: +1 if the agent cleans a dirty square.

### Heuristic Function ()

* **Logic**: The sum of Manhattan distances from the current position to **all remaining dirty squares**.

### Goal State

The search terminates successfully when **0 dirty squares** remain in the environment.

---

## 5. Frontier Grid World Details

### Data Storage

* **Grid Representation**: A 2D array of `Node` objects.
* **State Tracking**: Maintains a dynamic list/set of coordinates for **dirty nodes**.

### Key Checks

* **Goal Test**: Is the dirty node list empty?
* **Boundary Check**: Is the move within the [0, 4] index range?
* **State Check**: Is the current node `Dirty` or `Clean`?
* **Path ID**: Identifies nodes belonging to the final optimal path.

---

## 6. Key Functions

### `a_star_search()`

* **Finds Optimal Path**: Returns the sequence of moves to clean the entire grid.
* **Performance Metrics**:
* Counts **nodes expanded**.
* Counts **nodes in optimal path**.
* Calculates **total path cost**.


* **Action**: Simulates cleaning of dirty nodes as the path is traversed.

### `heuristic()`

* **Calculates **: Computes the estimated cost to reach the goal state.
* **Dirt Tracking**: Returns the count of remaining dirty nodes.
* **Distance Logic**: Computes distance from `current_node` to the nearest dirty node (or sum of all, depending on implementation).