# Problem 1: Maximum Sum Subarray of Size K

# Problem: Given an array of integers and a number k, 
# find the maximum sum of a subarray of size k.

# Input: arr = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].


# kadane's
arr = [2, 1, 5, 1, 3, 2]

k = 3
def brute_force(arr,k):
    mx_sum=float('-inf')
    sm=0
    for i in range(len(arr)-k+1):
        sm=0
        for j in range(i,k+i):
            sm+=arr[j]
            if mx_sum<sm:
                mx_sum=sm
    return mx_sum


def max_sum(arr,k):
    maximum_sum=sum(arr[:k])
    sm=sum(arr[:k])
    st=0
    end=k
    while end<len(arr):
        sm+=arr[end]
        sm-=arr[st]
        if maximum_sum<sm:
            maximum_sum=sm
        end+=1
        st+=1
    return maximum_sum
ans=max_sum(arr,k)
print(ans)
        
ans=brute_force(arr,k)
print(ans)  