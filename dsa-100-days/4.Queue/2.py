# 🚀 Day 48 of the 100 Days DSA Challenge 🎯
# Topic: Queue Problems 🏗️
# Problem Statement:
# You are given a queue data structure that supports the following operations:

# enqueue(x) → Adds an element x to the rear of the queue.
# dequeue() → Removes an element from the front of the queue.
# front() → Returns the front element without removing it.
# isEmpty() → Returns True if the queue is empty, otherwise False.
# Implement the above operations efficiently.

# Example:
# Input:
# plaintext
# Copy
# Edit
# enqueue(1)
# enqueue(2)
# enqueue(3)
# front()   # returns 1
# dequeue() # removes 1
# front()   # returns 2
# isEmpty() # returns False
# dequeue()
# dequeue()
# isEmpty() # returns True
# Output:
# plaintext
# Copy
# Edit
# 1
# 2
# False
# True
# Approaches:
# 1️⃣ Brute Force Approach (Using List with Shift Operations)
# Steps:
# Use a Python list to store queue elements.
# Use append(x) to enqueue elements at the end.
# Use pop(0) to dequeue elements from the front.
# Time Complexity:
# enqueue(x): O(1)
# dequeue(): O(N) (shifting elements after removing the front)
# Space Complexity: O(N)
# python
# Copy
# Edit
# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, x):
#         self.queue.append(x)

#     def dequeue(self):
#         if not self.isEmpty():
#             return self.queue.pop(0)
#         return -1  # Queue is empty

#     def front(self):
#         return self.queue[0] if not self.isEmpty() else -1

#     def isEmpty(self):
#         return len(self.queue) == 0

# # Example Usage
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.front())   # Output: 1
# print(q.dequeue()) # Output: 1
# print(q.front())   # Output: 2
# print(q.isEmpty()) # Output: False
# 2️⃣ Better Approach (Using Deque for Faster Removal)
# Steps:
# Use collections.deque instead of a list.
# append(x) for enqueue (rear insertion).
# popleft() for dequeue (front removal).
# Time Complexity:
# enqueue(x): O(1)
# dequeue(): O(1)
# Space Complexity: O(N)
# python
# Copy
# Edit
# from collections import deque

# class Queue:
#     def __init__(self):
#         self.queue = deque()

#     def enqueue(self, x):
#         self.queue.append(x)

#     def dequeue(self):
#         return self.queue.popleft() if not self.isEmpty() else -1

#     def front(self):
#         return self.queue[0] if not self.isEmpty() else -1

#     def isEmpty(self):
#         return len(self.queue) == 0

# # Example Usage
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.front())   # Output: 1
# print(q.dequeue()) # Output: 1
# print(q.front())   # Output: 2
# print(q.isEmpty()) # Output: False
# Hashtags for Your Journey:
# 📌 #DSAChallenge #100DaysOfDSA #DailyLearning #QueueImplementation #PythonDSA #CodingInterview #Queue 🚀







