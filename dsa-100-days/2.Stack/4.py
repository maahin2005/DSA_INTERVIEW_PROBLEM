from itertools import combinations

def removeKdigits(num, k):
    if len(num) == k:
        return "0"

    min_number = float('inf')

    for indices in combinations(range(len(num)), k):
        new_num = "".join([num[i] for i in range(len(num)) if i not in indices])
        min_number = min(min_number, int(new_num))

    return str(min_number)

# Example Usage
print(removeKdigits("1432219", 3))  # Output: "1219"
print(removeKdigits("10200", 1))    # Output: "200"
print(removeKdigits("10", 2))       # Output: "0"



def removeKdigits(num, k):
    num = list(num)
    
    for _ in range(k):
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:  
                num.pop(i)  
                break
        else:  
            num.pop()  
    
    result = "".join(num).lstrip("0")
    return result if result else "0"

# Example Usage
print(removeKdigits("1432219", 3))  # Output: "1219"
print(removeKdigits("10200", 1))    # Output: "200"
print(removeKdigits("10", 2))       # Output: "0"


def removeKdigits(num, k):
    stack = []
    
    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # Remove remaining k digits if necessary
    while k > 0 and stack:
        stack.pop()
        k -= 1
    
    # Convert stack to number string
    result = "".join(stack).lstrip("0")
    
    return result if result else "0"

# Example Usage
print(removeKdigits("1432219", 3))  # Output: "1219"
print(removeKdigits("10200", 1))    # Output: "200"
print(removeKdigits("10", 2))       # Output: "0"
