class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 특수문자 제거 & 대소문자 변경      
        s = re.sub('[^a-zA-Z0-9]','',s)
        s = s.lower() # s.upper()
        
        # re_slist = slist = list(s)
        # print(slist)
            
        # re_slist.reverse()
        # print(re_slist)
        
        # 문자열도 역순으로 변경 가능
        # print(s[::-1])
        # print(s)
                
        result = True        
        
        if s != s[::-1]:
            result = False
        
        return result
        