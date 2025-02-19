# Problem 5: Three Sum
# Problem: Given an integer array nums, 
# return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

nums = [-1,0,1,2,-1,-4]
#Time Complexity-O(n^3)
#Space Complexity-O(n^3)
def brute_force(arr):
    ans = set()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))  # Convert list to tuple and sort to avoid duplicates
                    ans.add(triplet)
    return ans

ans = brute_force(nums)
print(list(ans))  # Convert set back to list for printing


# Time Complexity: O(n^2)
# Space Complexity: O(1) (ignoring the space required for the output)

def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return res

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
