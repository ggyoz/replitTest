class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        arrlen = len(arr)        
        counterdict = dict(collections.Counter(arr).most_common())
        
        idx = 0
        
        for a in counterdict.keys():
            
            if arrlen <= len(arr) / 2:
                break
                
            arrlen -= counterdict[a]
            idx += 1
    
        return idx            
        