# 리스트에서 요소 찾기
# 없을경우 타겟넘버가 들어갈 자리 찾기

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        index = -1
        # 타겟넘버가 있을경우        
        if target in nums:
            index = nums.index(target)
        # 타겟넘버가 없을경우
        else:            
            if( nums[len(nums) - 1] < target ):
                index = len(nums)
            else:
                for a in range(len(nums)):                
                    if ( target < nums[a] ):
                        index = a
                        break
                    
        return index