# Find Peak Element
# Problem:A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element, and return its index. You may assume that nums[-1] = -∞ and nums[n] = -∞.

def find_peak_element(nums):
    left,right=0,len(nums)-1
    
    while left<right:
        mid=left+(right-left)//2
        
        if nums[mid]>nums[mid+1]:
            right=mid
        else:
            left=mid+1
        
        return left