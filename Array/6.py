# Find Minimum in Rotated Sorted 

# Problem:
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the rotated array nums, 
# return the minimum element.

def find_min(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]

# Time Complexity: O(log n)
# Space Complexity: O(1)
nums = [3, 4, 5, 1, 2]
print(find_min(nums))  # Output: 1