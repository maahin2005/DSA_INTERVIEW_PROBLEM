# Rotate an Array:
# Given an array, rotate it to the right by k steps.
# Example:
# Input: Array: [1, 2, 3, 4, 5], Steps: 2
# Output: [4, 5, 1, 2, 3]


def RotateArrKTimes(arr,k):
    rotate=k%len(arr)
    return arr[len(arr)-rotate:]+arr[:len(arr)-rotate]

arr= [1, 2, 3, 4, 5]
k=2
ans= RotateArrKTimes(arr,k)
print(ans)


def RotateArrKTimes(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > len(arr)
    
    # Helper function to reverse part of the array
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Reverse entire array
    reverse(0, n-1)
    # Reverse first k elements
    reverse(0, k-1)
    # Reverse the rest
    reverse(k, n-1)
    
    return arr

# Test Case
arr = [1, 2, 3, 4, 5]
k = 2
result = RotateArrKTimes(arr, k)
print(result)  # Output: [4, 5, 1, 2, 3]
