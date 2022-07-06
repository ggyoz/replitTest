from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = Counter(nums).most_common(1)
        
        return counter[0][0]

