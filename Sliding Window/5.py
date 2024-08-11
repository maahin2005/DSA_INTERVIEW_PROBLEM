# Problem 5: Fruits into Baskets
# Problem: Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.


# Input: fruits = ['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: The maximum number of fruits we can collect is 3 (['C', 'A', 'C']).

def total_fruit(fruits):
    window_start = 0
    max_fruits = 0
    fruit_frequency = {}
    
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1
        
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1
        
        max_fruits = max(max_fruits, window_end - window_start + 1)
    
    return max_fruits

# Example usage:
fruits = ['A', 'B', 'C', 'A', 'C']
print(total_fruit(fruits))  # Output: 3
