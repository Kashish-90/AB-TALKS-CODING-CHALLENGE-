# Day 43: Shortest Path in Binary Matrix

## 📌 Problem Statement

A city is represented as a binary matrix where `0` represents an open cell and `1` represents a blocked cell.

The task is to find the shortest path from the top-left corner to the bottom-right corner of the matrix while avoiding blocked cells.

This problem uses **Breadth-First Search (BFS)** to explore possible paths level by level and find the shortest path.

## 🎯 Objectives

* Solve the Shortest Path in Binary Matrix problem.
* Implement BFS traversal.
* Track visited locations to avoid repeated exploration.
* Visualize level-by-level exploration.
* Understand shortest-path algorithms in grid-based problems.

## 🧠 Approach: Breadth-First Search (BFS)

BFS explores all possible positions at the current distance before moving to positions farther away. Therefore, it finds the shortest path in an unweighted grid.

### Steps

1. Check whether the starting and destination cells are open.
2. Start BFS from the top-left cell.
3. Store each position and its distance in a queue.
4. Explore the eight neighboring cells, including diagonals.
5. Visit only cells that are inside the grid, open, and not previously visited.
6. Return the distance when the destination is reached.
7. If the queue becomes empty, return `-1` because no valid path exists.

## 💻 Python Implementation

```python
from collections import deque

def shortest_path(grid):
    n = len(grid)

    if n == 0 or grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    queue = deque([(0, 0, 1)])
    visited = {(0, 0)}

    while queue:
        row, col, distance = queue.popleft()

        if row == n - 1 and col == n - 1:
            return distance

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (0 <= new_row < n and
                0 <= new_col < n and
                grid[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                queue.append(
                    (new_row, new_col, distance + 1)
                )

    return -1

grid = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 1, 0]
]

print("Shortest path length:", shortest_path(grid))
```

## 📤 Output

```text
Shortest path length: 4
```

## 🧪 Example Explanation

Consider the following matrix:

```text
0  1  0
0  0  0
1  1  0
```

* Start at the top-left cell `(0, 0)`.
* Move down to `(1, 0)`.
* Move diagonally to `(1, 1)`.
* Move right to `(1, 2)`.
* Move down to the destination `(2, 2)`.

The shortest path contains **4 cells**, including the starting cell.

## ⏱️ Complexity Analysis

Let `N` be the number of rows and columns in the square matrix.

* **Time Complexity:** `O(N²)`
* **Space Complexity:** `O(N²)`

Each cell is visited at most once, and each cell has at most eight neighbors.

## 🌍 Real-World Applications

* GPS navigation and route planning.
* Robot movement and obstacle avoidance.
* Emergency evacuation systems.
* Delivery route optimization.
* Game pathfinding algorithms.

## 📚 Key Learnings

* Breadth-First Search (BFS).
* Queue-based graph traversal.
* Tracking visited cells.
* Finding shortest paths in unweighted graphs.
* Handling obstacles and grid boundaries.

## ✅ Conclusion

This challenge helped me understand how BFS explores a grid level by level to find the shortest path efficiently. It also demonstrated how graph traversal can solve practical navigation and pathfinding problems.

#ABTalks #DSA #Python #BFS #GraphTraversal #ShortestPath #CodingChallenge
