# Remove Duplicate

arr = [1,1,1,2,2,3,4]

#1. Brute Force Solution 

# Time Complexity: O(n^2)
# Space Complexity : O(n)
ans = []
for i in range(len(arr)):
   if arr[i] not in ans:
       ans.append(arr[i])
print(ans)
        

# 2. Better Solution 
# Time Complexity : O(n^2)
# Space Complexity : O(1)
arr = [1,1,1,2,2,3,4]
i=0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             arr.remove(arr[j])
# print(arr)

while i<len(arr)-1:
    if arr[i] == arr[i+1]:
        del arr[i]
    else:
        i+=1
print(arr)
        

      


# 3. Better Solution 
# Time Complexity: O(n)
# Space Complexity: O(1)
i=0
j=1
x=1

while j<len(arr):
	if arr[i] != arr[j]:
		arr[x] = arr[j]
		i = j
		x+=1
	j+=1
print(arr)