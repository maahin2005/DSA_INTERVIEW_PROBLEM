def asteroidCollision(asteroids):
    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break  
        else:
            stack.append(asteroid)

    return stack

# Example Usage
print(asteroidCollision([5, 10, -5]))  # Output: [5, 10]
print(asteroidCollision([8, -8]))      # Output: []
print(asteroidCollision([10, 2, -5]))  # Output: [10]
