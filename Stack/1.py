# 1. Valid Parentheses
# Problem:
# Given a string containing just the characters (, ), {, }, [ and ], determine if the input string is valid.


# Time Complexity: O(n)
# Space Complexity: O(n)
def is_valid(s):
    stack=[]
    for i in s:
        if i=='(' or i=='[' or i=='{':
            stack.append(i)
        elif stack and (stack[-1]=='(' and i==')' or stack[-1]=='{' and i=='}' or stack[-1]=='[' and i==']'):
            stack.pop()
        else:
            return False
        
    if stack:
        return False
    else:
        return True





s = "()[]{}"
print(is_valid(s))  # Output: True