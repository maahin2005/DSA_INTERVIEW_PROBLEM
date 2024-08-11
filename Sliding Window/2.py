# Problem 2: Longest Substring with K Distinct Characters
# Problem: Given a string, 
# find the length of the longest substring in it with at most K distinct characters.

# Input: s = "araaci", k = 2
# Output: 4
# Explanation: The longest substring with at most 2 distinct characters is "araa".

s = "araaci"
k = 2


def brute_force(s,k):
    ml=0
    for i in range(len(s)):
        a=[]
        for j in range(i,len(s)):
            a.append(s[j])
            if len(set(a))<=k and ml<len(a):
                ml=len(a)
    return ml                
# Time Complexity: O(n^3)
# Space Complexity: O(n)
ans=brute_force(s,k)
print(ans) 
           
# Time Complexity: O(n)
# Space Complexity: O(k)
def atmost_k_distinct(s,k):
    char_frequency={}
    window_start=0
    max_length=0
    for window_end in range(len(s)):
        right_char=s[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char]=0
        char_frequency[right_char]+=1
        
    while len(char_frequency)>k:
        left_char=s[window_start]
        char_frequency[left_char]-=1
        if char_frequency[left_char]==0:
            del char_frequency[left_char]
        window_start+=1
    max_length=max(max_length,window_end-window_start+1)
    return max_length

        
        