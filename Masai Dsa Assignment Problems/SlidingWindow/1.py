# Problem 1 .
# we have to find the maximum sum of k size in the array.

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
    

            
        
            