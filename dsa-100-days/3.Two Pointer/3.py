def canBeEqual(s1, s2):
    if s1 == s2:
        return True

    first, second = -1, -1

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if first == -1:
                first = i
            elif second == -1:
                second = i
            else:
                return False  # More than 2 mismatches

    return second != -1 and s1[first] == s2[second] and s1[second] == s2[first]

# Example Usage
print(canBeEqual("bank", "kanb"))  # Output: True
print(canBeEqual("attack", "defend"))  # Output: False
