# 441. Arranging Coins
# 합으로 계산한게 생각보다 느림

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        idx = 1
        
        while True:
            
            if n < idx:
                break
            
            n -= idx
            idx += 1
                
        return idx - 1

#         idx = 1            
#         while True:            
      
#             s = idx * (idx + 1) / 2            
#             if s >= n:                
#                 if s != n:
#                     idx -= 1      
#                 return idx                
                
#             idx += 1
        
        
                
                
                