
# 비효율적 코드
class Solution:
    def isValid(self, s: str) -> bool:
        
        answer = True
        
        if( len(s) % 2 != 0 ):
            return False
        else:            
            while 0 < len(s):
                
                temp = s                
                s = s.replace("{}", "").replace("()", "").replace("[]", "")

                if(temp == s):
                    answer = False
                    break
        
        return answer            



# 효율적인 코드