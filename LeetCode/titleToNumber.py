class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        cnt = 0        
        value = 0
        
        words = list(columnTitle)
        words.reverse()
        
        for word in words:
            
            value += (ord(word) - 64) * ( 26 ** cnt)
            cnt += 1
            
        return value            
            