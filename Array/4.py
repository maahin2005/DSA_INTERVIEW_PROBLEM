#  Container With Most Water
# Problem:
# Given n non-negative integers a1, a2, ..., an, 
# where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i are at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis, forms a container, such that the container contains the most water.


# Time Complexity: O(n)
# Space Complexity: O(1)


def max_area(height):
    max_area=float('-inf')
    
    i,j=0,len(height)-1
    
    while i<len(height) and j>=0:
        area=min(height[i],height[j])*(j-i)
        
        if area>max_area:
            max_area=area
            
        elif height[i]<height[j]:
            i+=1
        else:
            j-=1
    return max_area


# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))  # Output: 49