# 1. Longest Substring Without Repeating Characters
# Problem:
# Given a string s, find the length of the longest substring without repeating characters.


def Substring(s):
    max_len=1
    for i in range(len(s)):
        st=[]
        for j in range(i,len(s)):
            st.append(s[j])
            if len(st)==len(set(st)):
                max_len=max(max_len,len(st))
    return max_len

def length_of_longest_substring(s):
    map={}
    max_len=1
    start=0
    for i,char in enumerate(s):
        if char in map and map[char]>=start:
            start=map[char]+1
        max_len=max(max_len,i-start+1)
    
    return max_len


s = "abcabcbb"
# print(length_of_longest_substring(s))  # Output: 3
print(Substring(s))