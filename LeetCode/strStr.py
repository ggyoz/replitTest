class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
          
            hlist = list(haystack)
            for a in range(len(haystack)):                            
                if(("".join(hlist[a:a + len(needle)])) == needle):
                    return a
                  
        else:
            return -1
            