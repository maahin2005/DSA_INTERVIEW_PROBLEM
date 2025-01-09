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