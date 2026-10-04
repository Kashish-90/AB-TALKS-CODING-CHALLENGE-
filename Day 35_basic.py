# Advanced Sliding Window – Longest Unique Signal Pattern

## Problem Statement

A cybersecurity team intercepted a mysterious hacker signal.

The goal is to identify the longest substring without repeating characters before repetition corrupts the decoding process.

---

## Approach

This project uses the Sliding Window technique.

### Steps

1. Maintain a window of unique characters.
2. Expand the window using the right pointer.
3. If a duplicate character is found, shrink the window from the left.
4. Track the longest valid substring found.

---

## Example

Input:

```text
abcabcbb
```

Output:

```text
Longest Unique Signal Pattern: abc
Length: 3
```

---

## Time Complexity

O(n)

## Space Complexity

O(n)

---

## Real World Applications

* Cybersecurity signal analysis
* Network traffic monitoring
* Data compression systems
* Natural Language Processing (NLP)

---

## Author

Kashish Chhabra

AB Talks AI Challenge
