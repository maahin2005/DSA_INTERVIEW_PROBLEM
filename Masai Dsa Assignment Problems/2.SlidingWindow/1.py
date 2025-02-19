# Problem 1 .
# we have to find the maximum sum of k size in the array.
# Take out maximum
# Description
# Given an array of integers and a number k, find the maximum sum of a subarray of size k.

# First line consists of two integers n and k separated by space
# Second line consists of n integers separated by spaces.
# Constraints
# 1 <= n <= 10^7
# 1 <= k <= 10^6

# Print the maximum sum of a subarray of size k.

# 10 3
# -1 -1 -2 1 -2 4 1 9 3 9

# Output
# 21

arr = [2,4,1,4,6]
k= 3
# ans=11
#Brute Force Approach: 
# T.c = O(n*k)
# Sc = O(1)
def maxSum(arr,k):
   
    maxSum = float('-inf')
    for i in range(len(arr)-k +1):
        s=0
        for j in range(i,i+k):
            s+=arr[j]
        maxSum= max(maxSum,s)
    return maxSum

ans = maxSum(arr,k)
print(ans)


#Better Approach: 
#Tc = O(n)
#Sc = O(1)

s= sum(arr[:k])
maxSum = s

for i in range(len(arr)-k):
    s+= arr[i+k]-arr[i]
    maxSum = max(s,maxSum)
print(maxSum) 
    

            
        
            