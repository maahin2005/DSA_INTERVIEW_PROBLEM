# 2. Find Missing Number in Array (Math)
# 🔹 Problem Statement:
# You are given an array containing n-1 distinct integers in the range from 1 to n. Your task is to find the missing number in the array.
# Example:
# 1️⃣ Input:
# arr = [1, 2, 4, 5, 6], n = 6
# Output: 3
# Explanation: The number 3 is missing in the range 1 to 6.
# 2️⃣ Input:
# arr = [1, 3, 4, 5], n = 5
# Output: 2


# Time Complexity: O(n)
# Space Complexity: O(1)
def find_missing(arr, n):
 # Calculate total sum of numbers from 1 to n
 total = n * (n + 1) // 2
 # Subtract the sum of array elements from the total
 return total - sum(arr)