# Finding the Square Root of an Integer
# Problem:
# Given an integer x, return the square root of x rounded down to the nearest integer.

def sqrt(x):
    if x<2:
        return x
    
    left,right=2,x//2
    
    while left<=right:
        mid=left+(right-left)//2
        num=mid*mid
        
        if num==x:
            return mid
        elif num>x:
            right=mid-1
        else:
            left=mid+1
        
    return right

ans=sqrt(8)
print(ans)