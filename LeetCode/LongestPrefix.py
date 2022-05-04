class Solution:
    # def longestCommonPrefix(self, strs: [str]) -> str:            
        
    #     temp = 999
    #     str0 = ""
    #     answer = ""
        
    #     for s in strs:
            
    #         if( len(s) < temp ):
    #             temp = len(s)
    #             str0 = s
                
    #     flag = False        
    #     for a in range(temp):
    #         for st in strs:
                
    #             if(st[a] != str0[a]):
    #                 flag = True                
    #                 break                    
    #         if(flag):
    #                 break
    #         else:
    #             answer += str0[a]

    #     print(answer)
    #     return answer

      def longestCommonPrefix(self, strs: [str]) -> str:
          
          if not strs: return ""
          if len(strs) == 1: return strs[0]

          # 리스트에서 길이가 최소인 값 출력
          minStr = min(strs, key=len)
        
          i = len(minStr)
          counter = 0          
           
          while i > 0:            
              for j in range(len(strs)):                                  
                  if strs[j][:i:] == minStr[:i:]:
                      counter += 1
                      if counter == len(strs):
                          return minStr[:i:]
              i -= 1
              counter = 0
          return ""
    
            