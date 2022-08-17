class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # 모스부호 dictionary 생성       
        dic = {}
        
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for key, val in enumerate(mos):            
            dic[chr(key + 97)] = val

        # 집합에 모스부호 추가 ( 중복 제거 )
        moslist = set()
        
        for word in words:            
            mosstr = ''            
            for w in word:                
                mosstr += dic[w]                
            moslist.add(mosstr)        
        
        return len(moslist)