

def longest_subarray_with_sum(nums, target):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > target:
            current_sum -= nums[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example
nums = [4, 2, 1, 1, 6]
target = 8
print(longest_subarray_with_sum(nums, target))  # Output: 4
