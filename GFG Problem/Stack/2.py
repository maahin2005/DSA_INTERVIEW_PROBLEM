# 2. Min Stack
# Problem:Design a stack that supports push, pop, top, and retrieving 
# the minimum element in constant time.


# Time Complexity: O(1) for each operation
# Space Complexity: O(n)
class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
    def push(self,data):
        self.stack.append(data)
        if not self.min_stack or data<=self.min_stack[-1]:
            self.min_stack.append(data)
            
    def pop(self):
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        
    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
            
            
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # Output: -3
min_stack.pop()
print(min_stack.top())      # Output: 0
print(min_stack.get_min())  # Output: -2