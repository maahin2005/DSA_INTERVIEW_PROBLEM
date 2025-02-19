# 5. Longest Common Prefix
# Problem:
# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".



# Time Complexity: O(n * m) where n is the number of strings and m is the length of the longest prefix.
# Space Complexity: O(1)

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while s[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
        if not prefix:
            break
    
    return prefix

# Example usage:
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"