# Validate Binary Search Tree (BST)

## Project Overview

This project checks whether a binary tree follows the Binary Search Tree (BST) property.

A BST is a binary tree in which:

* Every value in the left subtree is smaller than the current node.
* Every value in the right subtree is greater than the current node.
* Both subtrees must also follow the BST property.

## Objectives

* Implement BST validation using Python.
* Track valid minimum and maximum ranges during traversal.
* Detect invalid tree structures.
* Test valid and invalid BST examples.

## Approach

The program uses recursion and range validation.

Each node is checked against a minimum and maximum allowed value. The left subtree receives an updated maximum, while the right subtree receives an updated minimum.

If any node violates its allowed range, the tree is invalid.

## Technologies Used

* Python 3
* Binary Trees
* Recursion
* Data Structures and Algorithms

## Complexity Analysis

* Time Complexity: O(n)
* Auxiliary Space Complexity: O(h), where h is the height of the tree.

## How to Run

1. Save the code in `validate_bst.py`.
2. Open a terminal in the project folder.
3. Run:

```bash
python validate_bst.py
```

## Learning Outcome

This project demonstrates recursive tree traversal, range checking, and validation of Binary Search Tree properties.
