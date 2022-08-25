# 383. Ransom Note
# a문자열이 b문자열 안에 전부 포함되어있는지 체크

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:                
        noteDict = dict(collections.Counter(ransomNote) - collections.Counter(magazine))        
        
        if not noteDict:
            return True
        
        return False

      # 1줄 컷
      # return not Counter(ransom_note) - Counter(magazine)