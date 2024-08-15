# 4. Group Anagrams
# Problem:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.



# Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string.
# Space Complexity: O(n * k)
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
   
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)
        print(anagrams,sorted_s)
    return list(anagrams.values())

# # Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))  # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]