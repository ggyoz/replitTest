class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
                
        # dp
        dp = [0] * (target + 1)        
        dp[0] = 1
        #print('dp:', dp)
        
        for t in range(1, target + 1):
            for num in nums:
                #print(t, num)
                if t >= num:                    
                    dp[t] += dp[t - num]
                    #print('dp:', dp)                           
        return dp[target]    
            
            
        
            
            