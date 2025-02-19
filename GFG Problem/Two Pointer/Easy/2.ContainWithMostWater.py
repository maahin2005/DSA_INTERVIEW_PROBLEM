# Problem 2: Container With Most Water
# Problem: Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i are at (i, ai) and (i, 0).
# Find two lines, which together with the x-axis forms a container, such that the container contains the most water.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

height = [1,8,6,2,5,4,8,3,7]


# Time Complexity: O(n)
# Space Complexity: O(1)
def container_with_most_water(height):
    i=0
    j=len(height)-1
    max_area=float('-inf')
    while i<j:
        min_height=min(height[i],height[j])
        width=j-i
        area=min_height*width
        max_area=max(max_area,area)
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return max_area

ans=container_with_most_water(height)
print(ans)