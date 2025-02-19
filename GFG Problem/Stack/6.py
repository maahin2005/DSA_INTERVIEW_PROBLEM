# 6. Next Greater Element
# Problem:
# Given an array nums, for each element, find the next greater element that is to the right of it in the array.


# Time Complexity: O(n)
# Space Complexity: O(n)
def next_greater_elements(nums):
    stack=[]
    ans=[-1]*len(nums)
    for i in range(len(nums)-2,-1,-1):
        while stack and nums[stack[-1]]<=nums[i]:
            stack.pop()
            
        if stack:
            ans[i]=nums[stack[-1]]
        stack.append(i)
    return ans

nums = [2, 1, 2, 4, 3]
print(next_greater_elements(nums))  # Output: [4, 2, 4, -1, -1]