# 1. Pair Sum (Two Sum in Sorted Array)
# Problem Statement
# Given a sorted array and a target sum, find two numbers that add up to the target.

# Example
# Input:
arr = [1, 2, 3, 4, 6]
target = 6
# Output:
# [1, 3]  # (Indexes in 0-based indexing)

ans = [-1,-1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            ans = [i,j]
            break
    if ans!=[-1,-1]:
        break
print(ans)


d={}
ans=[-1,-1]
for i in range(len(arr)):
    sec = target-arr[i]
    if sec in d:
        ans=[d[sec],i]
        break
    d[arr[i]]=i
print(ans)
        

def pairSumOptimal(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        sum_val = arr[left] + arr[right]
        if sum_val == target:
            return [left, right]
        elif sum_val < target:
            left += 1
        else:
            right -= 1
    return []
