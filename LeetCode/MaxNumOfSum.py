from collections import Counter

class Solution:
    def maxOperations(self, nums: [int], k: int) -> int:
      
        answer = 0      
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
            