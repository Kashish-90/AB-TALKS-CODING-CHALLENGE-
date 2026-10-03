# Maximum Average Subarray - Sliding Window

## Problem
Find the maximum average value of any contiguous subarray of size `k`.

## Approach

### Naive Method
- Calculate the sum of every window separately.
- Time Complexity: O(n*k)

### Sliding Window Method
- Compute the first window sum.
- Slide the window by removing the left element and adding the new right element.
- Keep track of the maximum sum.
- Time Complexity: O(n)

## Example

Input:
nums = [1, 12, -5, -6, 50, 3]
k = 4

Output:
12.75

## Learning Outcome
- Fixed-size Sliding Window
- Optimization from O(n*k) to O(n)
- Efficient handling of large datasets
