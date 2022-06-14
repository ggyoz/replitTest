class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxResult = currSum = nums[0]
        
        for num in nums[1:]:     
            
            #print(num, maxResult, currSum)
            
            currSum = max(currSum + num, num)
            maxResult = max(maxResult, currSum)
            
        
        return maxResult
                
            