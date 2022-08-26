# 290. Word Pattern
# 문자열과 패턴을 주고 문자열패턴이 주어진 패턴과 같은지 체크

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # 문자열 공백단위로 split
        word = s.split(' ')
        
        # 패턴과 길이 비교
        if len(pattern) != len(word):
            return False        
        
        # 문자열 dict
        strdict = {}        
        
        # 패턴 dict
        patterndict = {}
        patternlist = []
        
        # dict 인덱스
        idx1, idx2 = 0, 0
        
        # dict 입력
        for i, w in enumerate(word):
            
            if w not in strdict:
                strdict[w] = idx1
                idx1 += 1
            
            # print(pattern[i])
            if pattern[i] not in patterndict:
                patterndict[pattern[i]] = idx2
                idx2 += 1                
        
            word[i] = strdict[w]
            patternlist.append(patterndict[pattern[i]])
                    
        # print(patternlist)
        # print(word)
        
        if patternlist == word:
            return True
        
        return False
        