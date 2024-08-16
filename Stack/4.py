# 4. Largest Rectangle in Histogram
# Problem:
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
# find the area of the largest rectangle in the histogram.


#****

# Time Complexity: O(n)
# Space Complexity: O(n)
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Add a sentinel value to flush the stack at the end
    
    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

# Example usage:
heights = [2, 1, 5, 6, 2, 3]
print(largest_rectangle_area(heights))  # Output: 10
