# Problem of the Day: Maximum Sum Subarray of Size K
# Problem Statement:
# Given an array of integers and an integer K, find the maximum sum of any contiguous subarray of size K.

# Example:
# 1️⃣ Input:
# arr = [2, 1, 5, 1, 3, 2], K = 3
# Output: 9
# Explanation: The subarray [5, 1, 3] has the maximum sum of 9.

# 2️⃣ Input:
# arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0], K = 3
# Output: 16
# Explanation: The subarray [7, 8, 1] has the maximum sum of 16.

# Approaches:
# 1️⃣ Brute Force (Nested Loops)
# Logic:
# Calculate the sum of every possible subarray of size K. Keep track of the maximum sum.
# Time Complexity: O(n * K)
# Space Complexity: O(1)

# code 
def max_sum_subarray_brute(arr, K):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n - K + 1):
        current_sum = sum(arr[i:i+K])
        max_sum = max(max_sum, current_sum)
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
K = 3
print(max_sum_subarray_brute(arr, K))  # Output: 9

# 2️⃣ Sliding Window (Optimal Solution)
# Logic:
# Use a sliding window of size K.
# Maintain a running sum of the current window.
# Slide the window one step to the right by subtracting the first element of the window and adding the next element.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Code:

def max_sum_subarray_sliding_window(arr, K):
    n = len(arr)
    max_sum = float('-inf')
    current_sum = 0

    # Calculate the sum of the first window
    for i in range(K):
        current_sum += arr[i]

    max_sum = current_sum

    # Slide the window
    for i in range(K, n):
        current_sum += arr[i] - arr[i - K]
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [2, 1, 5, 1, 3, 2]
K = 3
print(max_sum_subarray_sliding_window(arr, K))  # Output: 9
