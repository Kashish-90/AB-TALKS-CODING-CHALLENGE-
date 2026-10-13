# Day 43: Course Schedule — Topological Sorting

## 📌 Problem Statement

A university has several courses with prerequisite requirements. We need to determine whether a student can complete all courses without getting stuck because of circular dependencies.

The task is to detect cycles in a directed dependency graph using **Breadth-First Search (BFS)** or **Depth-First Search (DFS)**.

## 🎯 Objectives

* Solve the Course Schedule problem.
* Detect cycles in a directed graph.
* Implement a solution using BFS and topological sorting.
* Understand prerequisite relationships.
* Apply graph algorithms to real-world dependency systems.

## 🧠 Approach: BFS (Kahn's Algorithm)

I used Kahn's Algorithm, which performs topological sorting using BFS.

### Steps

1. Create an adjacency list to represent course dependencies.
2. Calculate the indegree of every course. Indegree is the number of incoming prerequisite edges.
3. Add all courses with indegree `0` to a queue.
4. Remove a course from the queue and count it as completed.
5. Reduce the indegree of its dependent courses.
6. Add any dependent course whose indegree becomes `0` to the queue.
7. If all courses are processed, the schedule is possible. Otherwise, a cycle exists.

## 💻 Python Implementation

```python
from collections import deque

def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    queue = deque()

    for course in range(num_courses):
        if indegree[course] == 0:
            queue.append(course)

    completed = 0

    while queue:
        current = queue.popleft()
        completed += 1

        for neighbor in graph[current]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses

# Example 1: Possible schedule
print(can_finish(2, [[1, 0]]))

# Example 2: Circular dependency
print(can_finish(2, [[1, 0], [0, 1]]))
```

### Output

```text
True
False
```

## 🧪 Example Explanation

**Example 1**

There are two courses: `0` and `1`.

Prerequisite: Course `0` must be completed before Course `1`.

The schedule is possible, so the output is `True`.

**Example 2**

Course `0` depends on Course `1`, and Course `1` depends on Course `0`.

This creates a cycle, so neither course can be started. The output is `False`.

## ⏱️ Complexity Analysis

Let `V` represent the number of courses and `E` represent the number of prerequisite relationships.

* **Time Complexity:** `O(V + E)`
* **Space Complexity:** `O(V + E)`

## 🌍 Real-World Applications

* Package managers and software dependencies.
* CI/CD pipelines and build systems.
* University course scheduling.
* Task scheduling and project management.
* Detecting circular dependencies in applications.

## 📚 Key Learnings

* Directed graphs and adjacency lists.
* Indegree and dependency relationships.
* BFS traversal using a queue.
* Topological sorting using Kahn's Algorithm.
* Cycle detection in directed graphs.

## ✅ Conclusion

This challenge helped me understand how topological sorting can determine whether tasks or courses can be completed in the correct order. It also demonstrated how graph algorithms are used to identify circular dependencies in real-world systems.

#ABTalks #DSA #Python #GraphAlgorithms #TopologicalSorting #BFS #CodingChallenge
