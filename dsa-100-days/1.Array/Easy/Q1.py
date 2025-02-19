# Print all Distinct (Unique) Elements in given Array

# Given an integer array arr[], print all distinct elements from this array. The given array may contain duplicates and the output should contain every element only once.

# Examples: 

# Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
# Output: {12, 10, 9, 45, 2}


# Input: arr[] = {1, 2, 3, 4, 5}
# Output: {1, 2, 3, 4, 5}


# Input: arr[] = {1, 1, 1, 1, 1}
# Output: {1}

arr= [12, 10, 9, 45, 2, 10, 10, 45]


# 1. Brute force approach

# T.c = O(n^2)
# S.c = O(1)
def findDistinct(arr):
    res=[]
    for i in range(len(arr)):
        j=0
        while j<i:
            if arr[i]==arr[j]:
                break
            j+=1
        
        if i==j:
            res.append(arr[i])
    
    return res

ans=findDistinct(arr)
print(ans)


#2. Better 
#time complexity= O(n*logn) Time and 
#Space complexity=  O(n) 
def findDistinct(arr):
    res=[]
    arr.sort()
    for i in range(len(arr)):
        if i==0 or arr[i]!=arr[i-1]:
            res.append(arr[i])
            
    return res

ans=findDistinct(arr)
print(ans)           
        
    

# 3.

#t.c = O(n)
# S.c = O(n)
def findDistinct(arr):
    ans=[]
    for i in range(len(arr)):
        if arr[i] not in ans:
            ans.append(arr[i])
    return ans



#.4
#t.c = O(n)
# S.c = O(n)
print(list(set(arr)))
    