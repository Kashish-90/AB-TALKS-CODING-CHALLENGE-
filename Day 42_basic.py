# Day 42: Number of Islands

## Problem

Count the number of separate islands in a 2D grid. A cell containing `1` represents land, while `0` represents water. Land cells are connected only horizontally or vertically.

## Approach

I solved this problem using Depth-First Search (DFS).

1. Traverse every cell in the grid.
2. When unvisited land is found, increment the island counter.
3. Use DFS to visit all connected land cells.
4. Mark visited cells to avoid counting the same island again.
5. Return the total island count.

## Example

**Output:** `3`

## Complexity

* Time: O(R × C)
* Space: O(R × C)

## Concepts Learned

* Graph traversal
* Depth-First Search (DFS)
* Visited sets
* Connected components in a grid

## Key Learning

A single DFS traversal can explore an entire connected island. Every new unvisited land cell starts a new island.
