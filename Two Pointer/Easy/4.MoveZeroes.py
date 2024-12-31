# Problem 4: Move Zeroes
# Problem: Given an array nums,write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

nums = [0,1,0,3,12]


# Time Complexity: 𝑂(𝑛)
# Space Complexity: 𝑂(𝑛)

def BruteForce(arr):
    ans_arr = []  # O(1)
    for i in range(len(arr)):  # O(n)
        if arr[i] != 0:  # O(1) for each iteration
            ans_arr.append(arr[i])  # O(1) for each append
    
    n = len(arr) - len(ans_arr)  # O(1)
    ans_arr += [0] * n  # O(k), where k is the number of zeros, worst case O(n)
    
    return ans_arr

ans=BruteForce(nums)
print(ans)



# optimal-
# Time Complexity: O(n)
# Space Complexity: O(1)

def move_zeros(arr):
    zero_index=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[zero_index]=arr[zero_index],arr[i]
            zero_index+=1
    return arr

ans=move_zeros(nums)
print(ans)
