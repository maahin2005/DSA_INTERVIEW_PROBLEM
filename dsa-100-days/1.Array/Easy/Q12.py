def max_product_sliding_window(nums, k):
    if len(nums) < k:
        return -1  # Not enough elements for the window size

    max_product = float('-inf')
    current_product = 1
    zero_count = 0  # To handle zeros in the window

    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
            current_product = 1
        else:
            current_product *= nums[i]

        # Remove elements outside the current window
        if i >= k - 1:
            if zero_count == 0:
                max_product = max(max_product, current_product)
            # Slide the window
            if nums[i - k + 1] == 0:
                zero_count -= 1
            else:
                current_product //= nums[i - k + 1]

    return max_product

# Example
nums = [1, -2, -3, 4, -6, 2]
k = 3
print(max_product_sliding_window(nums, k))  # Output: 72 (subarray: [4, -6, 2])
