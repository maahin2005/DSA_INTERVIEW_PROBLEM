def max_area(height):
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        # Calculate the current area
        area = (r - l) * min(height[l], height[r])
        max_area = max(max_area, area)

        # Move the pointer pointing to the shorter height
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area

# Example Usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))  # Output: 49
