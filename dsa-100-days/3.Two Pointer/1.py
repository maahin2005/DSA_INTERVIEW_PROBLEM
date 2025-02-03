def longestStrictlyIncOrDec(nums):
    if not nums: return 0
    
    inc_len = dec_len = max_len = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            inc_len += 1
            dec_len = 1
        elif nums[i] < nums[i - 1]:
            dec_len += 1
            inc_len = 1
        else:
            inc_len = dec_len = 1  # Reset both for duplicate elements

        max_len = max(max_len, inc_len, dec_len)

    return max_len

# Example Usage
nums = [1,4,3,3,2]
print(longestStrictlyIncOrDec(nums))  # Output: 2
