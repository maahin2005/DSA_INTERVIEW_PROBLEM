def count_even_difference_partitions(nums):
    c = 0  # Counter for valid partitions
    total = sum(nums)  # Total sum of the array
    prefix = 0  # Prefix sum
    
    for i in range(len(nums) - 1):
        prefix += nums[i]  # Add current element to prefix sum
        left_sum = prefix
        right_sum = total - prefix
        difference = left_sum - right_sum
        
        if difference % 2 == 0:  # Check if the difference is even
            c += 1
    
    return c

# Example Usage
nums = [10, 10, 3, 7, 6]
print(count_even_difference_partitions(nums))  # Output: 4
