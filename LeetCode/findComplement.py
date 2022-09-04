# 476. Number Complement
# 2의 보수 계산

class Solution:
    def findComplement(self, num: int) -> int:

        binary = format(num, 'b')
        complement = ''

        for b in binary:

            if b == '0':
                complement += '1'
            else:
                complement += '0'

        return int(complement, 2)

########################################
# 비트연산자 XOR 활용방법
########################################
      
        # num = 5 일때

        # bin(num) = 101

        #print(num.bit_length()) => 3
        #print(bit_mask) => 7

        # 111
        bit_mask = 2**num.bit_length() - 1
        #print(format(bit_mask, 'b'))

        # 101 ^ 111 = 010
        return (num ^ bit_mask)
