# 10. Implement strStr()
# Problem:
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Time Complexity: O(n * m) in the worst case where n is the length of the haystack and m is the length of the needle.
# Space Complexity: O(1)
def str_str(haystack, needle):
    if not needle:
        return 0
    return haystack.find(needle)

# Example usage:
haystack = "hello"
needle = "ll"
print(str_str(haystack, needle))  # Output: 2