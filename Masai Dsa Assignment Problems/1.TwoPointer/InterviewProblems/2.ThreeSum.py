# 2. Three Sum
# Problem Statement
# Find triplets in an unsorted array that sum to zero.

# Example
# Input:
arr = [-1, 0, 1, 2, -1, -4]
# Output:
# [[-1, -1, 2], [-1, 0, 1]]


# Brute Force (O(N³))
ans=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i]+arr[j]+arr[k]==0:
                ans.append(tuple(sorted([i,j,k])))
print(ans)
                
# Optimal Approach (Sorting + Two Pointers, O(N²))

def threeSumOptimal(nums):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            sum_val = nums[i] + nums[left] + nums[right]
            if sum_val == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]: left += 1
                while left < right and nums[right] == nums[right - 1]: right -= 1
                left += 1
                right -= 1
            elif sum_val < 0:
                left += 1
            else:
                right -= 1
    return result

def threeSum(nums):
    nums.sort()
    n= len(nums)
    
    res = []
    
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
    
        left = i+1
        right = n-1
        
        while left<right:
            sumVal = nums[left]+nums[i]+nums[right]
            if sumVal ==0:
                res.append((nums[i],nums[right],nums[left]))
                while left < right and nums[left]==nums[left+1]:left+=1

                while left<right and nums[right] <nums[right-1]: right-=1
                
                left += 1
                right -= 1
                
            elif sumVal <0 :
                left+=1
            else:
                right -=1
    return res

ans = threeSum(arr)
print(ans)