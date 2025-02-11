def removeOccurrencesStack(s, part):
    stack = []
    part_length = len(part)

    for char in s:
        stack.append(char)  # Add to stack
        
        # Check if last `len(part)` characters form `part`
        if len(stack) >= part_length and "".join(stack[-part_length:]) == part:
            del stack[-part_length:]  # Remove `part` from stack

    return "".join(stack)

# Example Usage
print(removeOccurrencesStack("daabcbaabcbc", "abc"))  # Output: "dab"
print(removeOccurrencesStack("axxxxyyyyb", "xy"))  # Output: "ab"
