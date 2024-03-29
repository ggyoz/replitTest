class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        idx = 0
        zero = 0
        
        while idx < len(nums):            
            
            if nums[idx] == 0:
                nums.pop(idx)
                zero += 1
            else:
                idx += 1                
        
        nums.extend( [0] * zero )

      ################################################
      # two pointer
      
        i,j = 0,0
      
        for index in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        for i in range(j, len(nums)):
            nums[i] = 0
            