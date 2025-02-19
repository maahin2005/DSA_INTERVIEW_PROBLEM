
# 7. Remove K Digits
# Problem:
# Given a non-negative integer represented as a string num, remove k digits from the number so that the new number is the smallest possible.

# Solution:
#****

def remove_k_digits(num, k):
    stack = []
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # Remove remaining digits if k > 0
    while k:
        stack.pop()
        k -= 1
    
    # Remove leading zeros and convert to string
    return ''.join(stack).lstrip('0') or '0'

# Example usage:
num = "1432219"
k = 3
print(remove_k_digits(num, k))  # Output: "1219"
