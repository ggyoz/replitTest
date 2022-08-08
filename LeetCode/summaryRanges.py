class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        temp1 = temp2 = nums.pop(0)        
        
        ranges = []
        answer = []        
        
        while nums:
            
            temp2 = nums.pop(0)
            
            if temp2 - temp1 == 1:
                ranges.append(temp1)                
            else:
                ranges.append(temp1)
                
                if len(ranges) > 1:
                    answer.append(f"{ranges.pop(0)}->{ranges.pop()}")
                    ranges.clear()
                else:
                    answer.append(ranges.pop(0))
            
            temp1 = temp2
            
        
        print(ranges)
            
        
        
#         for idx in range(1, len(nums)):
            
#             print(nums[idx])
            
#             if nums[idx - 1] + 1 == nums[idx]:                
#                 if flag == False:
#                     temp += str(nums[idx - 1])
#                     flag = True                
                    
#             else:                
#                 if flag == False:
#                     answer.append(nums[idx - 1])
#                 else:
#                     temp += f"->{nums[idx - 1]}"
#                     answer.append(temp)
#                     temp = ""
#                     flag = False
        
        print(answer)
                
            
            