# 389. Find the Difference
# 주어진 문자열에 추가된 문자 찾기
# Counter로 찾기

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        return list(collections.Counter(t) - collections.Counter(s))[0]
        
