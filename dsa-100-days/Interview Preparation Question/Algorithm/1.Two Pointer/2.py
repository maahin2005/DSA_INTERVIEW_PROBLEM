#2. Target Sum

arr = [1,2,3,4,5,6,6,7,8,12]
target = 9
# ans = [0,8]
#1. Brute Force

ans = [-1,-1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == target:
            ans = [i,j]
            break
    if ans != [-1,-1]:
        break
print(ans)
            

# 2. Better Approach
# Time Complexity	O(n)
# Space Complexity	O(n)

# In Python, checking if a key exists in a dictionary using the in keyword has an average time complexity of O(1).

d = {}
ans = [-1,-1]
for i in range(len(arr)):
    sec = target - arr[i] 
    if sec in d:
        ans = [d[sec],i]
        break
    d[arr[i]] = i 
print(ans)

# 3. Optimal 
# Time complexity : O(n)
# Space complexity : O(1)


ans = [-1,-1]
i=0
j=len(arr)-1
while i<j:
    if arr[i] + arr[j] == target:
        ans = [i,j]
        break
    elif arr[i] + arr[j] < target:
        i+=1
    else:
        j-=1
print(ans)
    