class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNum(n):            
            r = 0            
            while n >= 1:
                r += (n % 10) ** 2
                n = n // 10                
            return r
        
        if n == 1:
            return True
        
        nums = []
        answer = False
        
        while n != 1:
            
            n = getNum(n)
            #print(n)

            if n == 1:
                answer = True
                break
            
            if n in nums:
                answer = False
                break
            else:
                nums.append(n)                
        
        return answer
        
       