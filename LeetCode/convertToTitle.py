class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
                
        num = list()        
        
        while columnNumber > 26:
                        
            if columnNumber % 26 != 0:
                num.append(columnNumber % 26)                
            else:  
                num.append(26)
                columnNumber -= 26                
                
            columnNumber = columnNumber // 26
            
        if columnNumber <= 26:
            num.append(columnNumber)
            
        num.reverse()
        
        print(num)
        
        answer = ""
        
        for a in num:
            answer += chr(a + 64)        
        
        return answer