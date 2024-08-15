from collections import Counter

def first_uniq_char(s):
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

# Example usage:
s = "leetcode"
print(first_uniq_char(s))  # Output: 0

# Time Complexity: O(n)
# Space Complexity: O(1)