# 2. Longest Palindromic Substring
# Problem:
# Given a string s, return the longest palindromic substring in s.

def Substring(s):
    long_st=''
    for i in range(len(s)):
        st=''
        for j in range(i,len(s)):
            st+=s[j]
            if st==st[::-1] and len(st)<len(long_st):
                long_st=st
    return long_st

                



# Time Complexity: O(n^2)
# Space Complexity: O(1)
def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    
    return longest


s = "babad"
print(longest_palindrome(s))  # Output: "bab" or "aba"

print(Substring(s))