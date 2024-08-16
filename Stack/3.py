# 3. Evaluate Reverse Polish Notation
# Problem:
# Evaluate the value of an arithmetic expression in Reverse Polish Notation. 
# The valid operators are +, -, *, /.


#****
# Time Complexity: O(n)
# Space Complexity: O(n)
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # token == '/'
                stack.append(int(a / b))  # Python division needs to be truncated towards zero
    return stack[0]

# Example usage:
tokens = ["2", "1", "+", "3", "*"]
print(eval_rpn(tokens))  # Output: 9
