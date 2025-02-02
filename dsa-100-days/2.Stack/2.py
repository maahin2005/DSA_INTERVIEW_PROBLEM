def largestRectangleArea(heights):
    heights.append(0)  # Sentinel to pop remaining elements
    stack, max_area = [], 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

# Example Usage
heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))  # Output: 10
