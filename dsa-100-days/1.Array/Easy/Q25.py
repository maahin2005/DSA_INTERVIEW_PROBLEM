def longest_distinct_substring(s):
    char_set = set()
    i, max_len = 0, 0

    for j in range(len(s)):
        while s[j] in char_set:  # Remove characters until no duplicate
            char_set.remove(s[i])
            i += 1
        char_set.add(s[j])  # Add current character to the set
        max_len = max(max_len, j - i + 1)

    return max_len

# Example
s = "abcabcbb"
print(longest_distinct_substring(s))  # Output: 3
