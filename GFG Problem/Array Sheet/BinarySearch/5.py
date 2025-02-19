# Search Insert Position
# Problem:
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

def search_insert(arr,target):
    left,right=0,len(arr)-1
    
    while left<=right:
        mid=left+(right-left)//2
        
        if arr[mid]==target:
            return mid
        
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
        
    return left

arr = [1, 3, 5, 6]
target = 5
target= 2
ans=search_insert(arr,target)
print(ans)