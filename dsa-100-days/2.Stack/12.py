#  Next Greater Element 

def nextGreaterElement(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):  # Traverse from right to left
        while stack and stack[-1] <= arr[i]:  
            stack.pop()  # Remove smaller elements
        result[i] = stack[-1] if stack else -1
        stack.append(arr[i])  # Push current element
    
    return result

# Example
arr = [4, 5, 2, 25]
print(nextGreaterElement(arr))  # Output: [5, 25, 25, -1]
