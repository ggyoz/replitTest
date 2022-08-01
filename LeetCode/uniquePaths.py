class Solution:
    def uniquePaths(self, m: int, n: int) -> int:        

      # 내가 푼 방법 ( 조합 )
        comA = list(range(max(m, n), max(m, n) + min(m, n) - 1))
        comB = list(range(2, min(m, n), 1))
        
        for b in range(len(comB)):
            for a in range(len(comA)):
                if comA[a] % comB[b] == 0:
                    #print(comA[a], comB[b], comA[a] // comB[b] )
                    comA[a] = comA[a] // comB[b]
                    comB[b] = 1
                    break                    
        
        x = self.multiply(comA)
        y = self.multiply(comB)
        
        return x // y        
        
    def multiply(self, arr):
        ans = 1
        for n in arr:
            if n == 0:
                return 0
            ans *= n
        return ans