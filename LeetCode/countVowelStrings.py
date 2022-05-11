class Solution:
    def countVowelStrings(self, n: int) -> int:
         
        N = 5
        dp = [1]*N
        
        print(dp)        
        
        
        for i in range(1,n):
            
            new_dp = [0]*N
            print('1111111111111')
          
            for j in range(N):
                
                print('------')                
                print(j)                
                
                for k in range(j+1):
                    
                    print('dp[]k',dp[k])                    
                    new_dp[j] += dp[k]
                    
            dp = new_dp[:]
            
        print(dp)    
            
        return sum(dp)