# 367. Valid Perfect Square
# sqrt함수 쓰지않고 제곱근 구하기

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if (num ** (1/2)) % 1 == 0:
            return True
        
        return False