# Topic: Implement Stack using Queues 🏗️
# Problem Statement:
# Design a stack using only queues (FIFO structure). Implement the following operations:

# push(x): Push element x onto the stack.
# pop(): Removes the top element.
# top(): Get the top element.
# empty(): Returns True if the stack is empty, else False.
# 🔹 Constraints:

# Implement using only queue operations (enqueue, dequeue, size, isEmpty).
# No use of built-in stack operations.
# Minimize the number of operations in each function.
# Example:

# Input: 
# push(1)
# push(2)
# top()     -> returns 2
# pop()     -> removes 2
# empty()   -> returns False
# Approaches:
# 1️⃣ Brute Force Approach (Using Two Queues, Push Efficient)
# Steps:
# Use two queues q1 (main) and q2 (temporary).
# push(x): Just enqueue to q1.
# pop(): Transfer n-1 elements from q1 to q2, remove the last one, then swap queues.
# top(): Same as pop(), but return the last element instead of deleting it.
# empty(): Check if q1 is empty.
# Time Complexity:
# push() → O(1) ✅
# pop() → O(N) ❌
# top() → O(N) ❌
# empty() → O(1) ✅
# Space Complexity: O(N)

from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1  # Swap queues
        return top_element

    def top(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1  # Swap queues
        return top_element

    def empty(self):
        return not self.q1

# Example Usage
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False

# 2️⃣ Better Approach (Using Two Queues, Pop Efficient)
# Steps:
# push(x): Transfer elements from q1 to q2, add x to q1, move elements back.
# pop(): Simply dequeue from q1.
# top(): Return q1[0].
# empty(): Check if q1 is empty.
# Time Complexity:
# push() → O(N) ❌
# pop() → O(1) ✅
# top() → O(1) ✅
# empty() → O(1) ✅

from collections import deque

class StackUsingQueuesEfficientPop:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())
    
    def pop(self):
        return self.q1.popleft() if self.q1 else -1
    
    def top(self):
        return self.q1[0] if self.q1 else -1
    
    def empty(self):
        return not self.q1

# Example Usage
stack = StackUsingQueuesEfficientPop()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False

# 3️⃣ Optimal Approach (Using Single Queue, Push Efficient)
# Steps:
# Use one queue only.
# push(x): Enqueue x, then rotate queue by n-1 times.
# pop(): Simply dequeue.
# top(): Return queue[0].
# empty(): Check if queue is empty.
# Time Complexity:
# push() → O(N) ❌
# pop() → O(1) ✅
# top() → O(1) ✅
# empty() → O(1) ✅

from collections import deque

class StackUsingSingleQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft() if self.q else -1

    def top(self):
        return self.q[0] if self.q else -1

    def empty(self):
        return not self.q

# Example Usage
stack = StackUsingSingleQueue()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False






