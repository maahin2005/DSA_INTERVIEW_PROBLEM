#  Product of Array Except Self
# Problem:
# Given an integer array nums, 
# return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].


#brute force
#t.c=O(n^2)
#Sc=O(n)
def product_except_self(nums):
    ans=[]
    for i in range(len(nums)):
        mul=1
        for j in range(len(nums)):
            if i!=j:
                mul*=nums[j]
        ans.append(mul)
    return ans
    

nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]


#prefix and postfix
#tc=O(n)
#sc=O(n)
def product_except_self(nums):
    pre=1
    ans=[1]*len(nums)
    
    for i in range(len(nums)):
        ans[i]=pre
        pre*=nums[i]
        
    post=1
    for i in range(len(nums)-1,-1,-1):
        ans[i]*=post
        post*=nums[i]
    
    return ans

print(product_except_self(nums))
    