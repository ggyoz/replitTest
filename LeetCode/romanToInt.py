# 로마숫자 변환
class Solution:
    def romanToInt(self, s: str) -> int:
        
        temp = 9999      
        answer = 0
        dic = { "M" : 1000, 
              "D" : 500, 
              "C" : 100, 
              "L" : 50, 
              "X" : 10, 
              "V" : 5, 
              "I" : 1 }        

        for a in s:            
            val = dic.get(a)
            if(val > temp):
                answer += (temp * -2)
            answer += val
            temp = val
            
        return answer        
    