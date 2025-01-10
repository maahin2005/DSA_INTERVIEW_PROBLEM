# 2. Kadane's Algorithm
# Kadane’s algorithm is used to find the maximum sum of a contiguous subarray.

def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # Output: 6 (subarray: [4, -1, 2, 1])
