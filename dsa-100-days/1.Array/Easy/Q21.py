def closest_sum(arr, target):
    arr.sort()  # Sort the array
    closest = float('inf')  # Initialize closest sum
    n = len(arr)
    
    for i in range(n - 2):
        left, right = i + 1, n - 1  # Two pointers
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            # Update closest sum if needed
            if abs(target - current_sum) < abs(target - closest):
                closest = current_sum
            
            # Move pointers based on the sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest  # Exact match
            
    return closest

# Example
arr = [-1, 2, 1, -4]
target = 1
print(closest_sum(arr, target))  # Output: 2
