# Time Complexity:O(log n), where n is the number of elements in the array.
# Space Complexity:O(1) for iterative approach.

def binary_search(arr,target):
    left,right=0,len(arr)-1
    
    while left<=right:
        mid=left+(right-left)//2
        
        # Check if the target is present at mid
        if arr[mid]==target:
            return mid
        
        elif arr[mid]>target:
            right=mid-1
        
        else:
            left=mid+1
            
    return -1


arr = [1, 3, 5, 7, 9, 11]
target = 7
result=binary_search(arr,target)

if result!=-1:
    print('Element is present at index',result)
else:
    print('Element is not present in array')
    