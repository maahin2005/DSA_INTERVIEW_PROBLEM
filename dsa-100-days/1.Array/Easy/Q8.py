# Problem: Remove Duplicates from Sorted Array
# 🔹 Problem Statement:
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once. The relative order of the elements must be maintained.
# Return the length of the new array with unique elements.

# 🔹 Example:
# Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]

# 🔹 Approach:

# Use the two-pointer technique:
# Maintain two pointers: one (i) tracks the position of the current unique element, while the other (j) traverses the array.
# Whenever a new unique element is encountered, update the position at i and increment it.
# 🔹 Time Complexity: O(N)
# 🔹 Space Complexity: O(1)
def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0  # Pointer for the position of the unique element
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:  # If a new unique element is found
            i += 1
            nums[i] = nums[j]  # Move the unique element to the next position

    return i + 1  # Length of the unique elements array

# Example
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
length = remove_duplicates(nums)
print(length)  # Output: 5
print(nums[:length])  # Output: [0, 1, 2, 3, 4]
