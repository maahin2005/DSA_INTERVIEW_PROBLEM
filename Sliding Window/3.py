# Problem 3: Smallest Subarray with a Given Sum
# Problem: Given an array of positive numbers and a positive number S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S.
# Return 0 if no such subarray exists.

# Input: arr = [2, 1, 5, 2, 3, 2], S = 7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

# Time Complexity: O(n)
# Space Complexity: O(1)

#My code
arr = [2, 1, 5, 2, 3, 2]
k = 7
def min_length_subarray(arr,k):
    sm=0
    min_length=len(arr)
    start=0
    for end in range(len(arr)):
        sm+=arr[end]
        
        while sm>=k and start<len(arr):
            sm-=arr[start]
            min_length=min(min_length,end-start+1)
            start+=1
            
    return min_length
        
ans=min_length_subarray(arr,k)
print(ans)


#chatGpt code
def smallest_subarray_with_given_sum(S, arr):
    window_sum = 0
    min_length = float('inf')
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        while window_sum >= S:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_length if min_length != float('inf') else 0

# Example usage:
arr = [2, 1, 5, 2, 3, 2]
S = 7
print(smallest_subarray_with_given_sum(S, arr))  # Output: 2
