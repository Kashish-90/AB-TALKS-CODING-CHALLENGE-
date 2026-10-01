Problem 1:[TWO SUM]
#Author-Kashish Chhabra
week 5 Sprint Challenge
#Time complexity:0(n)
#Space complexity:0(n)
def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
Problem 2:[MAXIMUM PROFIT]
#Author-Kashish Chhabra
week 5 Sprint Challenge
#Time complexity:0(n)
#Space complexity:0(1)
def max_profit(prices):

    min_price = prices[0]
    max_profit = 0

    for price in prices:

        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]

print(max_profit(prices))
#README.md
# Week 5 Sprint Challenge

## Overview

This repository contains my solutions for the AB Talks Week 5 Sprint Challenge.

The goal of this challenge was to solve two medium-level algorithm problems, analyze their time complexity, and explain the optimization decisions used to make the solutions scalable

# Problem 1: Two Sum

## Problem Statement

Given an array of integers and a target value, return the indices of the two numbers whose sum equals the target.

## Approach

### Brute Force Approach

Check every possible pair of elements using nested loops.

python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
This approach works but becomes slow for large arrays.

### Optimized Approach

I used a dictionary (hash map) to store previously seen numbers and their indices.

For each element:

1. Calculate the required complement.
2. Check if the complement already exists in the dictionary.
3. If found, return the indices.
4. Otherwise, store the current number.

This reduces the search operation from O(n) to O(1).
## Time Complexity

O(n)

The array is traversed only once.
## Space Complexity

O(n)

A dictionary is used to store elements and their indices.
## Why This Solution Scales

Instead of comparing every pair of elements, the hash map allows constant-time lookups.

For large datasets, O(n) performs significantly better than O(n²), making the solution more efficient and scalable.

---

# Problem 2: Best Time to Buy and Sell Stock

## Problem Statement

Given a list of stock prices, find the maximum profit that can be achieved by buying once and selling once.

## Approach

### Brute Force Approach

Compare every possible buy and sell pair.

```python
for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
```

This requires O(n²) time.

### Optimized Approach

Maintain:

* Minimum price seen so far
* Maximum profit found so far

For each price:

1. Update minimum price if a lower value is found.
2. Calculate current profit.
3. Update maximum profit if current profit is larger.

Only one traversal is required.
## Time Complexity

O(n)

The list is traversed once.
## Space Complexity

O(1)

Only a few variables are used.
## Why This Solution Scales

The algorithm avoids checking every buy-sell combination.

By tracking the minimum price and maximum profit in a single pass, it efficiently handles large datasets while using constant memory.
# Technologies Used

* Python 3
* Git
* GitHub
                                           
# Author

Kashish Chhabra

B.Tech Computer Science Engineering

AB Talks Python Challenge – Week 5 Sprint Challenge
