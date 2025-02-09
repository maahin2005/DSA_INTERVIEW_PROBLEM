def decodeString(s):
    stack = []
    num = 0
    current_string = ""

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == "[":
            stack.append((current_string, num))
            current_string = ""
            num = 0
        elif char == "]":
            prev_string, repeat_count = stack.pop()
            current_string = prev_string + repeat_count * current_string
        else:
            current_string += char

    return current_string

# Example Usage
print(decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(decodeString("3[a2[c]]"))   # Output: "accaccacc"
print(decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
