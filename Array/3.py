# Maximum Product Subarray
# Problem:
# Given an integer array nums,
# find the contiguous subarray within an array (containing at least one number) which has the largest product.

def max_product(nums):
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        result = max(result, max_prod)
    
    return result


# Time Complexity: O(n)
# Space Complexity: O(1)
def max_product(nums):
    max_product = min_product = result = nums[0]
    
    for num in nums[1:]:
        temp_max = max(num, max_product * num, min_product * num)
        min_product = min(num, max_product * num, min_product * num)
        max_product = temp_max
        result = max(result, max_product)
        
    return result
nums=[-1,-2,-3,-4]
print(max_product(nums))