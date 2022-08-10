class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # counters 사용
        counters = collections.Counter(nums)
        
        if len(counters) != len(nums):
            return True
        
        return False


        # set 사용
        # numset = set(nums)
      
        # if len(numset) != len(nums):
        #     return True
      
        # return False