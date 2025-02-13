#Stock Span Problem 
prices =[100,80,60,70,60,75,85]
# ans = [1,1,1,2,1,4,6]

#1. Brute Force Approach
def calculateSpan(prices):
    n=len(prices)
    spans=[1]*n    # initialize span arr with default values
    
    for i in range(1,n):
        j= i-1
        while j>=0 and prices[i]>=prices[j]:
            spans[i]+=1
            j-=1
    return spans

ans = calculateSpan(prices)
print(ans)

# Better Solution 

def calculateSpan(prices):
    n= len(prices)
    spans = [1]*n
    stack=[0]
    for i in range(1,n):
        while stack and prices[i]>=prices[stack[-1]]:
            stack.pop()
        spans[i]=i-stack[-1] if stack else i+1
        stack.append(i)
    return spans

ans = calculateSpan(prices)
print(ans)