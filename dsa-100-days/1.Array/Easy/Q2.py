# Given an unsorted array that may contain duplicates. Also given a number k which is smaller than the size of the array. Write a function that returns true if the array contains duplicates within k distance.
# Examples: 

# Input: k = 3, arr[] = {1, 2, 3, 4, 1, 2, 3, 4}
# Output: false
# All duplicates are more than k distance away.

# Input: k = 3, arr[] = {1, 2, 3, 1, 4, 5}
# Output: true
# 1 is repeated at distance 3.

# Input: k = 3, arr[] = {1, 2, 3, 4, 5}
# Output: false

# Input: k = 3, arr[] = {1, 2, 3, 4, 4}
# Output: true



#1. Brute Force
# T.C = O(n*k)
# S.C = O(1)
def duplicateWithinK(arr,k):
    for i in range(len(arr)):
        for j in range(1,k+1):
            c=i+j
            if c<len(arr) and arr[i]==arr[c]:
                return True
    return False

arr=[1, 2, 3, 4, 4]
k=3
ans= duplicateWithinK(arr,k)

print(ans)

#2. Better Approach
# T.c = O(n)
# S.c = O(n)
def duplicateWithinK(arr,k):
    ansSet= []
    for i in range(len(arr)):
        if arr[i] in ansSet:
            return True
        ansSet.append(arr[i])
        
        if(i>=k):
            ansSet.remove(arr[i-k])
    return False

arr =[1, 2, 3, 4, 5]
ans= duplicateWithinK(arr,k)

print(ans)
