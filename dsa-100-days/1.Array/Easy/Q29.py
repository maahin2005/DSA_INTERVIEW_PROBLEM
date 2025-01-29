def sortedSquares_better(nums):
    n = len(nums)
    left, right = 0, n - 1
    result = [0] * n
    index = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1
        index -= 1

    return result

# Example Usage
nums = [-4, -1, 0, 3, 10]
print(sortedSquares_better(nums))  # Output: [0, 1, 9, 16, 100]
