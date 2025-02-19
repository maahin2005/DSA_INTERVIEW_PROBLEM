def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point and divide the array into two halves
        mid = len(arr) // 2
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half

        # Recursively sort both halves
        merge_sort(L)
        merge_sort(R)

        # Initialize pointers for L, R, and the main array
        i = j = k = 0

        # Merge the sorted halves back into the original array
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any elements were left in L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Check if any elements were left in R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6]
merge_sort(arr)
print('merge_sort',arr)