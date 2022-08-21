class Solution:
    def isUgly(self, n: int) -> bool:        
      
        while n > 1:            
            if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
                answer = False
                break
            
            if n % 5 == 0:
                n //= 5
            
            if n % 3 == 0:
                n //= 3                
                
            if n % 2 == 0:
                n //= 2                
                
        if n == 1:
            return True
        else:
            return False

###############################################################

      # 배열 사용
        if n <= 0:
          return False
          
        for a in [2,3,5]:
            while n % a == 0:
                n =// a

        return n == 1
            
    