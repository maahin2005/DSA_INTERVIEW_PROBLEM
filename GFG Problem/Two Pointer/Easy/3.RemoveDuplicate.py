# Problem 3: Remove Duplicates from Sorted Array
# Problem: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length. 
# Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0, 1, 2, 3, 4]

nums = [0,0,1,1,1,2,2,3,3,4]
#time- O(n)
#Space- O(n)
def brute_force(nums):
    unique_arr=[]
    for i in range(len(nums)):
        if nums[i] not in unique_arr:
            unique_arr.append(nums[i])
    return unique_arr

ans=brute_force(nums)
print(ans)


# optimal-Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicate(arr):
    i=0
    j=1
    x=1
    while i<len(arr) and j<len(arr):
        if arr[i]!=arr[j]:
            arr[x]=arr[j]
            i+=1
            x+=1
        j+=1
    return arr[:x]

ans=remove_duplicate(nums)
print(len(ans),ans)
        