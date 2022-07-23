class Solution:
    def mySqrt(self, x: int) -> int:
        
        idx = 1
        
        while True:            
            a = idx * idx            
            if a == x:
                break
            elif a > x:
                idx -= 1
                break            
            idx += 1
    
        return idx
            
        