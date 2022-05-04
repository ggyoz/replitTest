from collections import Counter

class Solution:
    def maxOperations(self, nums: [int], k: int) -> int:
      
        answer = 0  
        # 카운터 자주나오니까 기억해두자
        counts = Counter(nums)

        if(k % 2 == 0):
            answer += counts[k // 2] // 2
            counts[k // 2] = 0        

        for a in counts:
            if a < k and k - a in counts:                
                answer += min(counts[a], counts[k - a])                
                counts[a] = 0
                counts[k - a] = 0

        print(counts)
      
        return answer
            