# Sum of subarray

# Description
# You are given an array of N integers and a single integer K. You need t o find out if there is a subarray, which has the sum exactly as K.
# First-line contains T, no of test cases.
# First-line of each test case contains N, the size of the array, and K.
# Second-line of each test casecontains N spaced integers, elements of an array.
# Constraints
# 1 <= N <= 10^5
# 1 <= K <= 10^12

# 3
# 5 3
# 1 2 1 3 4
# 4 5
# 1 2 1 3
# 3 2
# 1 2 1
arr=[1, 2, 1]
k=2
# Current Implementation: O(n)
# Worst Case: O(n³) (due to sum(a) inside the loop).
def targetK(arr,k):
    for i in range(len(arr)):
        a=[]
        for j in range(i,len(arr)):
            a.append(arr[j])
            print(a)
            s=sum(a)     
            if s==k:
                return True
    return False

ans = targetK(arr,k)
print(ans)
 

#better
#TC = O(n^2)
# Sc = O(1)   
def targetK(arr,k):
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s+=arr[j]     
            if s==k:
                return True
    return False

ans = targetK(arr,k)
print(ans)
    
# optimal approach
# Tc = O(n)
# Sc = O(1)
def targetK(arr,k):
    st=0
    end=0
    s=0
    while end<len(arr):
        s+=arr[end]
        while st<len(arr) and s>k:
            s-=arr[st]
            st+=1
        if s==k:
            return True
        end+=1
        
    return False

arr=[5,6,9,2,3]
k=110
ans = targetK(arr,k)
print(ans)