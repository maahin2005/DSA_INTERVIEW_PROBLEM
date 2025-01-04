# Find the all substring of a string.

# Example
# 1️⃣ Input: "abc"
# Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
# Explanation:

# Substrings: "a", "ab", "abc", "b", "bc", "c"
# 2️⃣ Input: "abcd"
# Output: ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']






def all_substrings(s):
    n = len(s)
    substrings = []
    for i in range(n):
        for j in range(i + 1, n + 1):  # End index goes up to n+1 to include the last character
            substrings.append(s[i:j])
    return substrings

# Example
print(all_substrings("abc"))  
# Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
