# Problem Statement: Reverse an Array
# You are given an array of integers. Your task is to reverse the elements of the array in-place, such that the last element becomes the first, the second-last becomes the second, and so on.


# Example 1:
# Input:
# n=5
# arr=[1, 2, 3, 4, 5]
# Output:
# [5 4 3 2 1]

# Example 2:
n=6
arr=[10,20,30,40,50,60]


# brute force

revArr= [-1]*n
for i in range(len(arr)-1,-1,-1):
    revArr[n-i-1]=arr[i]
print(revArr)


# better 

i=0
j=n-1
while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1
print(arr)