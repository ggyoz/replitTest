class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def getIso(word):
            
            iso = {}        
            s = []
            idx = 0
            
            for w in word:
                
                if w not in iso:
                    iso[w] = idx
                    idx += 1
                
                #s += str(iso[w])
                s.append(iso[w])
            
            return s
                
        #print(getIso(s))
        #print(getIso(t))        
        
        if getIso(s) == getIso(t):
            return True
        else:
            return False