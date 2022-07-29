class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:        
        
        dic1 = self.getPattern(pattern)        
        len(dic1)
        answer = list()
        
        for word in words:            
            dic2 = dict()
            dic2 = self.getPattern(word)
            
            if dic1 == dic2:
                answer.append(word)
                
        return answer
      
    # Dictionary로 문자를 숫자로 변환
    def getPattern(self, word: str):                
        
        index = 0
        patt = dict()        
        chword = ''
        
        for w in word:
            
            if not w in patt:            
                patt[w] = index
                index += 1
        
            chword += str(patt[w])
            
        return chword    
            