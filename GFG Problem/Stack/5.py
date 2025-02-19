# 5. Trapping Rain Water
# Problem:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



# Time Complexity: O(n)
# Space Complexity: O(n)
def trap(height):
    stack = []
    water_trapped = 0
    
    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(h, height[stack[-1]]) - height[top]
            water_trapped += distance * bounded_height
        stack.append(i)
    
    return water_trapped

# Example usage:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))  # Output: 6
