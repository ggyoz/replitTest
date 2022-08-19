class Solution:
    def addDigits(self, num: int) -> int:
      
        while num > 9:            
            
            num = sum( int(n) for n in str(num) )
            print(num)
            
            # a = 0
            # for n in str(num):
            #     a += int(n)
            # num = a
          
        return num