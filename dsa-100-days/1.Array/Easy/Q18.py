# 🎯 Day 18 Completed! 🚀 Arrays - 100 Days of DSA Challenge

# Problem of the Day: Alternative Approach for Two Sum or Difference
# 🌟 Problem Statement:
# You are given an unsorted array of integers and a target value. Your task is to find two numbers in the array such that their sum equals the target or their difference equals the target. Solve the problem without using the two-pointer technique.

# Optimal Solution (Using Hashing)
# Code Implementation:
# python
# Copy
# Edit
# def find_pair_with_sum_or_diff(arr, target):
#     seen = set()  # Set to store visited elements

#     for num in arr:
#         # Check for sum
#         if target - num in seen:
#             return [target - num, num]
#         # Check for difference
#         if num - target in seen or target + num in seen:
#             return [num, num - target] if num - target in seen else [num, target + num]
        
#         # Add the current number to the set
#         seen.add(num)

#     return "No such pair found"

# # Example
# arr = [4, 7, 1, 10, 12, 8]
# target = 5
# print(find_pair_with_sum_or_diff(arr, target))  # Output: [7, 12]
# Time Complexity:
# O(N): Single traversal of the array with constant time lookups in the set.
# Space Complexity:
# O(N): Space required for the hash set to store visited elements.
# Explanation of the Hashing Approach:
# Use a hash set (seen) to store numbers as you iterate through the array.
# For every number in the array, check:
# If target - num exists in the set, a pair is found for the sum condition.
# If num - target or num + target exists in the set, a pair is found for the difference condition.
# If no pair is found after processing all elements, return that no such pair exists.
# Practice Challenge:
# 🌟 Problem Statement:
# Given an array of integers, find two numbers whose product equals a given target value.

# Example:

# Input: arr = [2, 4, 1, 6, 5, 40], target = 20
# Output: [4, 5]
# You’re making excellent progress! Each day adds a new layer to your problem-solving skills. Keep going! 🚀


def find_pair_with_sum_or_diff(arr, target):
    seen = set()  # Set to store visited elements

    for num in arr:
        # Check for sum
        if target - num in seen:
            return [target - num, num]
        # Check for difference
        if num - target in seen or target + num in seen:
            return [num, num - target] if num - target in seen else [num, target + num]
        
        # Add the current number to the set
        seen.add(num)

    return "No such pair found"

# Example
arr = [4, 7, 1, 10, 12, 8]
target = 5
print(find_pair_with_sum_or_diff(arr, target))  # Output: [7, 12]





