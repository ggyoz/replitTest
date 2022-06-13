class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        value = 0        
        prev = prices[0]        
        
        for a in range(1, len(prices)):
            
            if value < (prices[a] - prev):
                value = prices[a] - prev
            
            if prev > prices[a]:                
                prev = prices[a]
                
        return value