# 🚀 Day 46 of the 100 Days DSA Challenge 🎯
# Topic: Valid Parentheses 🏗️
# Problem Statement:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# A string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket before it.
# 🔹 Constraints:

# 1 ≤ s.length ≤ 10^4
# s consists only of '(){}[]'
# Example:
# Input 1:
# s = "()"
# Output:
# True
# Input 2:
# s = "()[]{}"
# Output:
# True
# Input 3:
# s = "(]"
# Output:# False
# Approaches:
# 1️⃣ Brute Force Approach (Replace Pairs Iteratively)
# Steps:
# While s contains "()", "{}", or "[]", remove them from s.
# If the final string is empty, return True; else, return False.
# Time Complexity: O(N^2) ❌ (due to repeated removals)
# Space Complexity: O(1)



def isValid(s):
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""

# Example
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False

# 2️⃣ Better Approach (Using Stack)
# Steps:
# Use a stack to track opening brackets.
# Traverse s, and for every opening bracket, push it onto the stack.
# For every closing bracket, check:
# If the stack is empty, return False.
# If the top of the stack has the matching opening bracket, pop it.
# Otherwise, return False.
# In the end, return True if the stack is empty.
# Time Complexity: O(N) ✅
# Space Complexity: O(N) ✅



def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}  # Matching pairs
    
    for char in s:
        if char in mapping:  # If it's a closing bracket
            top = stack.pop() if stack else '#'  # Get the top element or '#' if empty
            if mapping[char] != top:
                return False  # Mismatched pair
        else:
            stack.append(char)  # Push opening bracket

    return not stack  # Stack should be empty if valid

# Example
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False

# 📌 #DSAChallenge #100DaysOfDSA #DailyLearning #ValidParentheses #Stack #BracketsValidation #CodingInterview # 🚀







