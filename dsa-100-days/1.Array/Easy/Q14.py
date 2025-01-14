# def min_window_substring(s, t):
#     from collections import Counter

#     if not t or not s:
#         return ""

#     char_count = Counter(t)
#     required = len(char_count)
#     left, right = 0, 0
#     formed = 0
#     window_counts = {}
#     min_length = float("inf")
#     min_window = ""

#     while right < len(s):
#         char = s[right]
#         window_counts[char] = window_counts.get(char, 0) + 1

#         if char in char_count and window_counts[char] == char_count[char]:
#             formed += 1

#         while left <= right and formed == required:
#             if (right - left + 1) < min_length:
#                 min_length = right - left + 1
#                 min_window = s[left:right + 1]

#             window_counts[s[left]] -= 1
#             if s[left] in char_count and window_counts[s[left]] < char_count[s[left]]:
#                 formed -= 1

#             left += 1

#         right += 1

#     return min_window

# # Example
# s = "ADOBECODEBANC"
# t = "ABC"
# print(min_window_substring(s, t))  # Output: "BANC"


# def max_consecutive_ones(nums):
#     left = 0
#     max_ones = 0
#     zero_count = 0

#     for right in range(len(nums)):
#         if nums[right] == 0:
#             zero_count += 1

#         while zero_count > 1:
#             if nums[left] == 0:
#                 zero_count -= 1
#             left += 1

#         max_ones = max(max_ones, right - left + 1)

#     return max_ones

# # Example
# nums = [1, 0, 1, 1, 0, 1]
# print(max_consecutive_ones(nums))  # Output: 4
