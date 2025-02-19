def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching in the left half
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result

arr = [2, 4, 4, 4, 6, 7]
target = 4
ans=first_occurrence(arr,target)
print(ans)