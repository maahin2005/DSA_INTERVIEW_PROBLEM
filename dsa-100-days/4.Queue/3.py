# 🚀 Day 49 of the 100 Days DSA Challenge 🎯
# Topic: Min Stack (Stack with Minimum Element Retrieval in O(1)) 🏗️
# Problem Statement:
# Design a stack that supports the following operations efficiently:

# push(x) → Push element x onto the stack.
# pop() → Remove the top element.
# top() → Get the top element.
# getMin() → Retrieve the minimum element in the stack in O(1).
# Example:
# Input:
# plaintext
# Copy
# Edit
# push(5)
# push(3)
# push(7)
# push(2)
# getMin()   # returns 2
# pop()      # removes 2
# getMin()   # returns 3
# pop()      # removes 7
# top()      # returns 3
# Output:
# plaintext
# Copy
# Edit
# 2
# 3
# 3
# Approaches:
# 1️⃣ Brute Force Approach (Using List, Linear Search for Min)
# Steps:
# Use a normal list stack to store elements.
# Find the minimum element by iterating over stack whenever getMin() is called.
# Time Complexity:
# push(x): O(1)
# pop(): O(1)
# top(): O(1)
# getMin(): O(N) (traversing the stack to find the minimum)
# Space Complexity: O(N)
# python
# Copy
# Edit
# class MinStack:
#     def __init__(self):
#         self.stack = []

#     def push(self, x):
#         self.stack.append(x)

#     def pop(self):
#         if self.stack:
#             self.stack.pop()

#     def top(self):
#         return self.stack[-1] if self.stack else -1

#     def getMin(self):
#         return min(self.stack) if self.stack else -1

# # Example Usage
# minStack = MinStack()
# minStack.push(5)
# minStack.push(3)
# minStack.push(7)
# minStack.push(2)
# print(minStack.getMin())  # Output: 2
# minStack.pop()
# print(minStack.getMin())  # Output: 3
# print(minStack.top())     # Output: 3
# 2️⃣ Better Approach (Using Auxiliary Min Stack)
# Steps:
# Maintain an extra minStack that stores the minimum at each push.
# On pop(), remove from minStack as well.
# getMin() returns the top of minStack in O(1).
# Time Complexity:
# push(x): O(1)
# pop(): O(1)
# top(): O(1)
# getMin(): O(1)
# Space Complexity: O(N)
# python
# Copy
# Edit
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, x):
#         self.stack.append(x)
#         if not self.minStack or x <= self.minStack[-1]:
#             self.minStack.append(x)

#     def pop(self):
#         if self.stack:
#             if self.stack[-1] == self.minStack[-1]:
#                 self.minStack.pop()
#             self.stack.pop()

#     def top(self):
#         return self.stack[-1] if self.stack else -1

#     def getMin(self):
#         return self.minStack[-1] if self.minStack else -1

# # Example Usage
# minStack = MinStack()
# minStack.push(5)
# minStack.push(3)
# minStack.push(7)
# minStack.push(2)
# print(minStack.getMin())  # Output: 2
# minStack.pop()
# print(minStack.getMin())  # Output: 3
# print(minStack.top())     # Output: 3
# Hashtags for Your Journey:
# 📌 #DSAChallenge #100DaysOfDSA #DailyLearning #MinStack #Stack #DataStructures #CodingInterview #Python 🚀







