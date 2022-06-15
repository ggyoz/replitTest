class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxResult = currSum = nums[0]
        
        for num in nums[1:]:     
            
            #print(num, maxResult, currSum)            
            currSum = max(currSum + num, num)
            maxResult = max(maxResult, currSum)
            
        
        return maxResult
                
        # # Kadane algorithm
        # maxi=nums[0]
        # sums=0
        # for i in range(len(nums)):
        #     sums+=nums[i]
        #     maxi=max(sums,maxi)
        #     if sums<0:
        #         sums=0
        # # print(maxi)
        # return maxi     