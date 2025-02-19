# Problem 4: Maximum Number of Vowels in a Substring of Given Length
# Problem: Given a string s and an integer k,
# return the maximum number of vowel letters in any substring of s with length k.

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

s = "abciiidef"
k = 3
st=0
c_vowel=0
c_vowel+=sum(1 for char in s[:k] if char in 'aeiou')
max_vowel=c_vowel
end=k
while end<len(s):
    if s[end] in 'aeiou':
        c_vowel+=1
    if s[st] in 'aeiou':
        c_vowel-=1
    
    max_vowel=max(max_vowel,c_vowel)
    st+=1
    end+=1
print(max_vowel)



#chatgpt code
# Time Complexity: O(n)
# Space Complexity: O(1)

def max_vowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    window_start, max_vowels_count, current_vowels_count = 0, 0, 0
    
    for window_end in range(len(s)):
        if s[window_end] in vowels:
            current_vowels_count += 1
        
        if window_end >= k:
            if s[window_start] in vowels:
                current_vowels_count -= 1
            window_start += 1
        
        max_vowels_count = max(max_vowels_count, current_vowels_count)
    
    return max_vowels_count

# Example usage:
s = "abciiidef"
k = 3
print(max_vowels(s, k))  # Output: 3
