# 3. Valid Anagram
# Problem:
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.


#time-O(nlogn)
#space-O(1)
def is_anagram(s,t):
    if sorted(s)==sorted(s):
        return True
    return False

s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # Output: True

