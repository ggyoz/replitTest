
# LeetCode 
# 9. Palindrome Number

class Solution:
  
    def isPalindrome(self, x: int) -> bool:
        
        if x > 0:
            temp = x
            r = []
            while temp > 0:
                r.append(temp % 10)
                temp = temp // 10

            org = r[::-1]
            
            return org == r            
            
        elif x == 0:
            return True
        else:
            return False 

