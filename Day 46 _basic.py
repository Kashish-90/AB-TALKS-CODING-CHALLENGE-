# 🤖 Minimum Cost Climbing Stairs — Dynamic Programming

## 📌 Project Overview

This project solves the **Minimum Cost Climbing Stairs** problem using Dynamic Programming (DP).

Imagine a robot travelling across dangerous rooftops. Each step consumes energy, and the robot must find the path that uses the minimum energy to reach its destination.

The goal is to calculate the minimum total cost required to reach the top while avoiding unnecessary energy consumption.

## 🎯 Objectives

* Solve the Minimum Cost Climbing Stairs problem.
* Understand recursion versus Dynamic Programming.
* Store intermediate results to avoid repeated calculations.
* Visualize state transitions in DP.
* Optimize the solution for better time complexity.

## ⚙️ Features

* Calculates the minimum climbing cost.
* Uses Dynamic Programming to store previously computed results.
* Demonstrates an optimized approach.
* Explains the transition between states.
* Compares recursive and DP-based solutions.

## 🧠 Concepts Used

* Dynamic Programming
* Recursion
* Arrays
* Memoization
* Tabulation
* Time and Space Complexity

## 🛠️ Technologies Used

* **Language:** Python
* **IDE:** VS Code
* **Version Control:** Git and GitHub

## 💡 Problem Explanation

You are given an array `cost`, where `cost[i]` represents the energy required to step on stair `i`.

You can climb either one or two steps at a time. The objective is to reach the top with the minimum total cost.

### Example

**Input:**

```python
cost = [10, 15, 20]
```

**Output:**

```text
15
```

**Explanation:**

You can start from stair 0 or stair 1.

* Starting from stair 0 costs 10, then jumping to the top costs no additional stair energy.
* Starting from stair 1 costs 15 and jumping directly to the top costs no additional stair energy.

The minimum cost is **15**.

## 🔄 Dynamic Programming Approach

Define `dp[i]` as the minimum cost required to reach stair `i`.

The recurrence relation is:

```text
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
```

The final answer is:

```text
min(dp[n-1], dp[n-2])
```

This approach reuses previously calculated results instead of repeatedly solving the same subproblems.

## ⏱️ Complexity Analysis

For a bottom-up DP solution:

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

The space complexity can be optimized to **O(1)** by storing only the previous two results.

## 🌍 Real-World Applications

Dynamic Programming is useful in:

* Robotics and path planning
* Resource optimization
* Financial planning
* Logistics and scheduling
* AI decision-making systems

## 📚 What I Learned

* How Dynamic Programming works.
* The difference between recursion and DP.
* How to store intermediate results.
* How to optimize time and space complexity.
* How to solve minimum-cost optimization problems.

## 👩‍💻 Author

**Kashish Chhabra**

## ⭐ Acknowledgement

This project is part of my 60-day coding challenge to improve my programming and Data Structures and Algorithms skills.
