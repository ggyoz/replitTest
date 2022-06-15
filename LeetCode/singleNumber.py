class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        
        answer = 0        
        
        for no in range(len(nums)):
            
            answer = nums.pop()
            
            if answer in nums:
                nums.remove(answer)
            else: 
                break
                
        return answer