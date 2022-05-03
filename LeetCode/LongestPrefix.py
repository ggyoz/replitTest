class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:        
        
        temp = 999
        str0 = ""
        answer = ""
        
        for s in strs:
            
            if( len(s) < temp ):
                temp = len(s)
                str0 = s
                
        flag = False        
        for a in range(temp):
            for st in strs:
                
                if(st[a] != str0[a]):
                    flag = True                
                    break                    
            if(flag):
                    break
            else:
                answer += str0[a]

        print(answer)
        return answer
    
            