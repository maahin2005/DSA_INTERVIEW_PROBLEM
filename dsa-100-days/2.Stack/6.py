def simplifyPath(path):
    stack = []
    for part in path.split("/"):
        if part == "..":
            if stack:
                stack.pop()
        elif part and part != ".":
            stack.append(part)

    return "/" + "/".join(stack)

# Example Usage
print(simplifyPath("/home/"))       # Output: "/home"
print(simplifyPath("/../"))         # Output: "/"
print(simplifyPath("/home//foo/"))  # Output: "/home/foo"
print(simplifyPath("/a/./b/../../c/"))  # Output: "/c"
