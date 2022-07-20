class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
                
        result = len(words)
        
        for word in words:            
            # find 시작위치 초기화
            index = -1
            
            for w in word:
                # find 시작위치를 갱신함
                index = s.find(w, index + 1)
                
                # 찾지못할경우
                if index == -1:
                    result += -1
                    break
        
        return result