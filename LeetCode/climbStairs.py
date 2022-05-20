class Solution:
    def climbStairs(self, n: int) -> int:
        
        cal = [1, 2]
        
        if(n <= 2):
            return n
        
        else:
            
            for _ in range(n - 2):
                cal.append(cal[-1] + cal[-2])
            
        return cal[-1]