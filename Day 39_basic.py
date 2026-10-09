# Maximum Depth of Binary Tree

## Project Overview

This project calculates the maximum depth of a binary tree using Python.

The maximum depth is the number of nodes along the longest path from the root node to a leaf node.

## Objectives

* Implement the Maximum Depth of Binary Tree problem.
* Understand recursive depth calculation.
* Explore Depth-First Search (DFS).
* Handle edge cases such as an empty tree and a single-node tree.

## Approach

The program uses recursion to calculate the depth of the left and right subtrees.

If the tree is empty, the function returns 0. Otherwise, it returns 1 plus the greater depth of the two subtrees.

## Technologies Used

* Python 3
* Binary Trees
* Recursion
* Depth-First Search (DFS)

## Complexity Analysis

* Time Complexity: O(n)
* Auxiliary Space Complexity: O(h), where h is the height of the tree.

## How to Run

1. Save the code as `maximum_depth.py`.
2. Open the terminal in the project folder.
3. Run the command:

```bash
python maximum_depth.py
```

## Learning Outcomes

* Understanding binary tree structures.
* Implementing recursion.
* Calculating tree depth using DFS.
* Handling edge cases in tree problems.
