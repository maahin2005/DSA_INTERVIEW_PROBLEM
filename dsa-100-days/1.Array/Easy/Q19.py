def move_zeros_to_end(arr):
    n = len(arr)
    non_zero_index = 0

    # Move all non-zero elements to the front
    for i in range(n):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1

    return arr

# Example
arr = [0, 1, 0, 3, 12]
print(move_zeros_to_end(arr))  # Output: [1, 3, 12, 0, 0]
