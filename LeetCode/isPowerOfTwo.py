class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        #### while문 사용 ####
        # while n > 1:

        #       if n % 2 != 0:
        #           return False
        #       else:
        #           n = n / 2

        #   if n == 1:
        #       return True

        #### for문 사용 ####
        # for a in range(32):

        #       if n == 2 ** a:
        #           return True

        #   return False

        #### 재귀 ####
        # if n == 1:
        #     return True

        # if n == 0 or n % 2 != 0:
        #     return False

        # return self.isPowerOfTwo(n / 2)

        #### log 활용 ####
        if n <= 0:
            return False
        else:
            return (math.log10(n) / math.log10(2)) % 1 == 0
