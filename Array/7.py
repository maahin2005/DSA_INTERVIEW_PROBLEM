# Majority Element
# Problem:
# Given an array nums of size n, return the majority element. 
# The majority element is the element that appears more than n/2 times.

#bruteforce
#tc=O(n^2)
#sc=O(1)
def majority_element(nums):
    
    for i in range(len(nums)):
        if nums.count(nums[i])>len(nums)//2:
            return nums[i]
    return -1
    


nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))  # Output: 2


# Time Complexity: O(n)
# Space Complexity: O(1)
def majority_element(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

# Example usage:
nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))  # Output: 2
