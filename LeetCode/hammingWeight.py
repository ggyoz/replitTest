class Solution:
    def hammingWeight(self, n: int) -> int:
                        
        answer = 0
        
        for a in str(format(n, 'b')):
            if a == '1':
                answer += 1
                
        return answer

      # 다른풀이1
      # return str(bin(n)).count('1')

      # 다른풀이2
      # res = 0        
      # while n:
      #   n = n & (n - 1) # Removing no of 1 bits only
      #   res += 1
      # return res