maxSum = float("-inf")
        s=0
        j=0
        i=0
        while i<len(nums) and j<len(nums):
            s=0
            while j==len(nums)-1  or (j<len(nums) and nums[j]<nums[j+1]):
                j+=1
            s = sum(nums[i:j+1])
            maxSum = max(s,maxSum)
            i= j+1
            j+=1
        return maxSum

                        
