class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        # 최소공배수
        L = lcm(p,q)        
        
        print(L)
        
        if (L // q) % 2 == 0:
            return 2
        

        return (L // p) % 2