# Problem 1: Two Sum II - Input Array Is Sorted
# Problem: Given an array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. Return the indices of the two numbers (1-indexed).

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

numbers = [2,7,11,15]
target = 9

#brute force
def BruteForce(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            return [i+1,j+1]
    return [-1,-1]
 
ans=BruteForce(numbers,target)
print(ans)

# better code-
# Time Complexity: O(n)
# Space Complexity: O(n)


def twoSum(nums,target):
    d={}
    for i in range(len(nums)):
        reqVal = target- nums[i]
        if reqVal in d:
            return [d[reqVal]+1,i+1]
        d[nums[i]]=i
    return [-1,-1]

ans=twoSum([2,7,11,15],9)
print(ans)
#optimize code  -
# Time Complexity: O(n)
# Space Complexity: O(1)

 
def two_sum(arr,k):
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]+arr[j]==k:
            return [i+1,j+1]
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1
    return [-1,-1]

ans=two_sum(numbers,target)
print(ans)



            
        
    