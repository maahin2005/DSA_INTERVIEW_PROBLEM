# Finding the Last Occurrence of a Target in a Sorted Array
# Problem:Given a sorted array, find the last occurrence of a target element.

arr = [2, 4, 4, 4, 6, 7] 
target = 4

def last_ocurrence(arr,target):
    left=0
    right=len(arr)-1
    res=-1
    
    while left<=right:
        mid=left+(right-left)//2
        
        if arr[mid]==target:
            res=mid
            left=mid+1
            
        elif arr[mid]<target:
            left=mid+1
            
        else:
            right=mid-1
    
    return res
    
ans=last_ocurrence(arr,target)
print(ans)
        
        