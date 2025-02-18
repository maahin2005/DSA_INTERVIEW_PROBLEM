# Subarrays Having Sum Less Than M

# Description
# Given an array A of size n with positive numbers, find the total number of subarrays that have sum < m.
# Font Size: 18
# Input
# The first line of the input contains one integer t (1 ≤ t ≤ 10) - the numb er of test cases. Then t test cases follow.
# The first line of each test case contains a single integer n (1 ≤ n ≤ 1000 00) and M as mentioned in the question.
# The second line of the test case contains n integers (1 ≤ Ai ≤ 100).
# Output
# For each test case, print the answer. The number of subarrays.
# Sample Input 1
# 1
# 55
# Sample Output 1
# 5
# 15132

arr = [1,5,1,3,2]
k=5
def targetK(arr,k):
    c=0
    for i in range(len(arr)):
        a=[]
        for j in range(i,len(arr)):
            a.append(arr[j])
            s=sum(a)     
            if s<k:
                c+=1
    return c

ans = targetK(arr,k)
print(ans)
 
 
# Better 
#Tc = O(n^2)
#Sc = O(1)
arr = [1,5,1,3,2]
k=5
def targetK(arr,k):
    c=0
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s+=arr[j]     
            if s<k:
                c+=1
    return c

ans = targetK(arr,k)
print(ans)
 
 
#optimal
#Tc = O(n)
# Sc = O(1) 
arr = [1,5,1,3,2]
k=5
st=0
end=0
c=0
s=0
while end<len(arr):
    s+=arr[end]
    while st<len(arr) and s>=k:
        s-=arr[st]
        st+=1
    if s<k:
        c+= end-st+1
    end+=1

print(c)