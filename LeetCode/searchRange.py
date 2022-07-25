class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # 내가 푼 방법
      
        starting = -1
        ending = -1
        
        for i in range(len(nums)):
            
            if nums[i] == target:
                
                if starting == -1:
                    starting = i
                    
                ending = i
        
        return [starting, ending]        
        