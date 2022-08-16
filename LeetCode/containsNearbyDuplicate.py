class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dict={}
        
        for key,val in enumerate(nums):            
            
            #print(key, val)
			
            if val in dict and (key - dict[val] ) <= k:
                return True
            
            dict[val] = key
            
        return False


# time out
#         for i in range(0, len(nums)):            
#             for j in range(i + 1, len(nums)):
                
#                 #print(i ,j)
                
#                 if math.abs(j - i) > k:
#                     break
                
#                 if nums[i] == nums[j]:
#                     return True        
        
#         return False