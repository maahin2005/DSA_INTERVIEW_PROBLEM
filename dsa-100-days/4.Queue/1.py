# 🚀 Day 47 of the 100 Days DSA Challenge 🎯
# Topic: Implement Queue using Stacks 🏗️
# Problem Statement:
# Implement a queue using two stacks.

# Implement the following operations:

# push(x): Pushes element x to the back of the queue.
# pop(): Removes the element from the front of the queue.
# peek(): Returns the front element of the queue.
# empty(): Returns True if the queue is empty, otherwise False.
# 🔹 Constraints:

# 1 ≤ x ≤ 10^9
# At most 100 operations will be performed.
# All calls to pop() and peek() are valid (i.e., no pop from an empty queue).
# Example:
# Input 1:



# push(1)
# push(2)
# peek()   # returns 1
# pop()    # returns 1
# empty()  # returns False
# Output:



# 1
# 1
# False
# Approaches:
# 1️⃣ Brute Force Approach (Using a Single Stack & Recursion)
# Steps:
# Push elements onto a stack normally.
# When popping, use recursion to remove the bottom-most element (which represents the front of the queue).
# Time Complexity:
# push(): O(1)
# pop(): O(N) (since recursion is used to remove the oldest element)
# Space Complexity: O(N) (due to recursion stack)



class QueueUsingStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 1:
            return self.stack.pop()
        val = self.stack.pop()
        last = self.pop()
        self.stack.append(val)
        return last

    def peek(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0

# Example
q = QueueUsingStack()
q.push(1)
q.push(2)
print(q.peek())  # Output: 1
print(q.pop())   # Output: 1
print(q.empty()) # Output: False

# 2️⃣ Better Approach (Using Two Stacks with Lazy Transfer)
# Steps:
# Use two stacks (stack1 for push, stack2 for pop).
# When popping, move elements from stack1 to stack2 only if stack2 is empty.
# Time Complexity:
# push(): O(1)
# pop(): O(1) amortized
# peek(): O(1)
# empty(): O(1)



class MyQueue:
    def __init__(self):
        self.stack1 = []  # Push stack
        self.stack2 = []  # Pop stack

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self.peek()
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2

# Example
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # Output: 1
print(q.pop())   # Output: 1
print(q.empty()) # Output: False









