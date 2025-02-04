# # 🚀 Day 35 of the 25 Days DSA Challenge
# # Topic: Longest Strictly Increasing or Strictly Decreasing Subarray
# # Problem Statement:
# # You are given an array of integers nums. Return the length of the longest subarray of nums that is either strictly increasing or strictly decreasing.

# # Example 1:



# # Input: nums = [1,4,3,3,2]
# # Output: 2
# # Explanation:
# # The strictly increasing subarrays are: [1], [4], [1,4]
# # The strictly decreasing subarrays are: [4], [3], [3,2], [4,3]
# # Longest subarray is [1,4] or [3,2] → Length = 2
# # Example 2:



# Input: nums = [3,3,3,3]
# Output: 1
# # Explanation:
# # All elements are the same, so the longest strictly increasing or decreasing subarray is just any single element.
# # Approaches:
# # 1️⃣ Brute Force Approach (Check All Subarrays)
# # Steps:
# # Generate all subarrays of nums[].
# # For each subarray, check if it is strictly increasing or strictly decreasing.
# # Keep track of the maximum length found.
# # Time Complexity: O(N²)
# # Space Complexity: O(1)



# def longestStrictlyIncOrDec(nums):
#     n = len(nums)
#     max_len = 1  # At least one element is always a valid subarray

#     for i in range(n):
#         # Check increasing sequence
#         for j in range(i + 1, n):
#             if nums[j] > nums[j - 1]:
#                 max_len = max(max_len, j - i + 1)
#             else:
#                 break  # Not increasing anymore

#         # Check decreasing sequence
#         for j in range(i + 1, n):
#             if nums[j] < nums[j - 1]:
#                 max_len = max(max_len, j - i + 1)
#             else:
#                 break  # Not decreasing anymore

#     return max_len

# # Example Usage
# nums = [1,4,3,3,2]
# print(longestStrictlyIncOrDec(nums))  # Output: 2
# 2️⃣ Better Approach (Using Two Passes)
# Steps:
# Maintain an increasing counter (inc_len) and decreasing counter (dec_len).
# Iterate through nums[], checking:
# If nums[i] > nums[i-1], increase inc_len, reset dec_len.
# If nums[i] < nums[i-1], increase dec_len, reset inc_len.
# Otherwise, reset both.
# Keep track of the maximum value of both counters.
# Time Complexity: O(N)
# Space Complexity: O(1)
# python


# def longestStrictlyIncOrDec(nums):
#     n = len(nums)
#     if n == 0: return 0

#     inc_len, dec_len = 1, 1
#     max_len = 1

#     for i in range(1, n):
#         if nums[i] > nums[i - 1]:
#             inc_len += 1
#             dec_len = 1  # Reset decreasing sequence
#         elif nums[i] < nums[i - 1]:
#             dec_len += 1
#             inc_len = 1  # Reset increasing sequence
#         else:
#             inc_len = dec_len = 1  # Reset both for equal elements

#         max_len = max(max_len, inc_len, dec_len)

#     return max_len

# # Example Usage
# nums = [1,4,3,3,2]
# print(longestStrictlyIncOrDec(nums))  # Output: 2
# 3️⃣ Optimal Approach (Using a Single Pass)
# Steps:
# Initialize max_len = 1, inc_len = 1, and dec_len = 1.
# Traverse the array once:
# If nums[i] > nums[i-1], increase inc_len and reset dec_len.
# If nums[i] < nums[i-1], increase dec_len and reset inc_len.
# If nums[i] == nums[i-1], reset both counters.
# Maintain max_len = max(max_len, inc_len, dec_len).
# Return max_len.
# Time Complexity: O(N)
# Space Complexity: O(1)
# python


# def longestStrictlyIncOrDec(nums):
#     if not nums: return 0
    
#     inc_len = dec_len = max_len = 1

#     for i in range(1, len(nums)):
#         if nums[i] > nums[i - 1]:
#             inc_len += 1
#             dec_len = 1
#         elif nums[i] < nums[i - 1]:
#             dec_len += 1
#             inc_len = 1
#         else:
#             inc_len = dec_len = 1  # Reset both for duplicate elements

#         max_len = max(max_len, inc_len, dec_len)

#     return max_len

# # Example Usage
# nums = [1,4,3,3,2]