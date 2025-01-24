# product of array except self

arr = [1,2,3,4]
n=4

mul = 1
for i in range(n):
    mul*=arr[i]
newArr = [mul]*n
# print(newArr)
for i in range(n):
    newArr[i] //= arr[i]

print(*newArr)


# 2nd method 

pre = 1
ans = [1]*n
for i in range(n):
    ans[i] = pre
    pre *= arr[i]

# print(ans)
post = 1
for i in range(n-1,-1,-1):
    ans[i]*=post 
    post *= arr[i]
    
print(*ans)