# Lowest Common Ancestor (LCA) of a Binary Search Tree

## 📌 Project Overview

This project implements the Lowest Common Ancestor (LCA) algorithm for a Binary Search Tree (BST) using Python.

The goal is to find the lowest node in the tree that is an ancestor of two given nodes.

## 🎯 Objectives

* Implement the LCA algorithm for a BST.
* Understand BST traversal and node comparisons.
* Visualize the ancestor relationship between nodes.
* Analyze the time and space complexity.

## 🛠️ Technologies Used

* Python 3
* Binary Search Tree (BST)
* Git and GitHub

## ⚙️ How It Works

The algorithm starts from the root and compares the two target values with the current node.

* If both values are smaller, it moves to the left subtree.
* If both values are larger, it moves to the right subtree.
* Otherwise, the current node is the Lowest Common Ancestor.

## 🌳 Example

BST values: `[20, 10, 30, 5, 15, 25, 35, 12, 18]`

* First node: `12`
* Second node: `18`
* Lowest Common Ancestor: `15`

## ⏱️ Complexity Analysis

* **Time Complexity:** O(h), where h is the height of the tree.
* **Auxiliary Space Complexity:** O(1) for the iterative implementation.

For a balanced BST, the time complexity is O(log n). In the worst case, it is O(n).

## 🚀 How to Run

1. Install Python 3.
2. Save the program as `lca_bst.py`.
3. Open a terminal in the project folder.
4. Run:

   `python lca_bst.py`

## 📚 What I Learned

* How a Binary Search Tree works.
* How to compare node values strategically.
* How to find the Lowest Common Ancestor efficiently.
* How to analyze algorithm complexity.
* How to document and submit a Python project using GitHub.

## 👩‍💻 Author

Kashish Chhabra
