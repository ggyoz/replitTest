class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        
        # newnums = list()
        # newnums.append(nums[0])        
        
        # for n in range(1, len(nums)):
            
        #     if nums[n-1] != nums[n]:
        #         newnums.append(nums[n])
        
        # nums = newnums
        
        # print(nums)

        # num = ''
        # tmp = nums[:]
        
        # for n in tmp:
            
        #     if n == num:
        #         nums.remove(n)
        #     num = n               
        
        # return len(nums)

        nums[:] = sorted(set(nums))        
        return len(nums)
        
        