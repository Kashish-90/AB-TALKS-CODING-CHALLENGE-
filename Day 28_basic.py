import time

# Brute Force Approach
def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Optimized Hashing Approach
def two_sum_optimized(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i

    return []


# Sample Treasure Map Coordinates
nums = [2, 7, 11, 15]
target = 9


# Brute Force Timing
start = time.time()
result1 = two_sum_bruteforce(nums, target)
end = time.time()

print("Brute Force Result:", result1)
print("Brute Force Time:", end - start)


# Optimized Timing
start = time.time()
result2 = two_sum_optimized(nums, target)
end = time.time()

print("Optimized Result:", result2)
print("Optimized Time:", end - start)
