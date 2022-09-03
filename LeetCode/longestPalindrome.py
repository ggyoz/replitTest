# 409. Longest Palindrome
# counter 활용 회문최대길이 계산

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        c = collections.Counter(list(s))
        
#         for key, value in enumerate(c):            
#             print(key, value)

        middle = 0
        answer = 0

        for key in c:
            
            if c[key] == 1:
                middle = 1
            
            if c[key] > 1 and c[key] % 2 == 0:
                answer += c[key]
            elif c[key] > 1 and c[key] % 2 != 0:
                answer += c[key] - 1
                middle = 1                
        
        return answer + middle
            
            
        
        