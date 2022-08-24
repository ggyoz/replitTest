# 344. Reverse String
# 투포인터 활용해서 문자 배열 순서 바꾸기 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """        
        start = 0
        end = len(s) - 1
        
        while start < end:
            
            s[start], s[end] = s[end], s[start]            
            start += 1
            end -= 1
        