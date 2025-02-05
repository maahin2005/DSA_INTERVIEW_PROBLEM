#1. Bruteforce Approach
def canBeEqual(s1, s2):
    if s1 == s2:
        return True

    n = len(s1)
    for i in range(n):
        for j in range(i, n):
            s1_list = list(s1)
            s1_list[i], s1_list[j] = s1_list[j], s1_list[i]  # Swap
            if "".join(s1_list) == s2:
                return True

    return False

# Example Usage
print(canBeEqual("bank", "kanb"))  # Output: True
print(canBeEqual("attack", "defend"))  # Output: False

#2. Better Approach
def canBeEqual(s1, s2):
    if s1 == s2:
        return True

    diff = []
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append((s1[i], s2[i]))

    if len(diff) == 2 and diff[0] == diff[1][::-1]:  # Swap check
        return True

    return False

# Example Usage
print(canBeEqual("bank", "kanb"))  # Output: True
print(canBeEqual("attack", "defend"))  # Output: False


#3. Optimal approach
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
