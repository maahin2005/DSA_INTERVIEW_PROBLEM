# Sum of all Subarrays
# Last Updated : 26 Nov, 2024
# Given an integer array arr[], find the sum of all sub-arrays of the given array. 

# Examples: 

# Input: arr[] = [1, 2, 3]
# Output: 20
# Explanation: {1} + {2} + {3} + {2 + 3} + {1 + 2} + {1 + 2 + 3} = 20


# Input: arr[] = [1, 2, 3, 4]
# Output: 50

#1. BruteForce
# TC =O(n^2)
# Sc = O(1)
def sumOfAllSubarrays(arr):
    totalSum =0
    for i in range(len(arr)):
        temp=0
        for j in range(i,len(arr)):
            temp+=arr[j]
            totalSum+=temp
            
    return totalSum
arr = [1, 2, 3]
print(sumOfAllSubarrays(arr))  


#2. Better
# Tc =O(n)
# Sc =O(1)
def sumOfAllSubarrays(arr):
    totalSum=0
    for i in range(len(arr)):
        totalSum+= arr[i]*(i+1)*(len(arr)-i)
    return totalSum

arr = [1, 2, 3]
print(sumOfAllSubarrays(arr))  

            
            