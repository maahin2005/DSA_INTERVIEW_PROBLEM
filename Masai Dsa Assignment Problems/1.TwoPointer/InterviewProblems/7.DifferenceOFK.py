# 🔹 Difference of K - Problem Statement
# 📝 Problem Description
# Given a sorted array of integers arr and an integer k, find all pairs (arr[i], arr[j]) where:

# ∣
# 𝑎
# 𝑟
# 𝑟
# [
# 𝑖
# ]
# −
# 𝑎
# 𝑟
# 𝑟
# [
# 𝑗
# ]
# ∣
# =
# 𝑘
# ∣arr[i]−arr[j]∣=k
# That is, the absolute difference between the two elements is exactly k.

# 🔹 Example 1
# Input:
# python
# Copy
# Edit
# arr = [1, 2, 3, 5, 7, 9]  
# k = 2
# Output:
# python
# Copy
# Edit
# [(1, 3), (3, 5), (5, 7), (7, 9)]
# Explanation:
# |1 - 3| = 2
# |3 - 5| = 2
# |5 - 7| = 2
# |7 - 9| = 2
# 🔹 Example 2
# Input:
# python
# Copy
# Edit
# arr = [1, 4, 6, 8, 10]  
# k = 4
# Output:
# python
# Copy
# Edit
# [(1, 5), (4, 8), (6, 10)]
# Explanation:
# |1 - 5| = 4
# |4 - 8| = 4
# |6 - 10| = 4
# 🔹 Constraints
# The array is sorted in ascending order.
# The array contains unique elements.
# The size of the array is 1 ≤ n ≤ 10⁵.
# k ≥ 0.
