class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = int("".join(map(str, digits))) + 1
        
        answer = []
        
        while num > 0:
            r = num % 10            
            answer.insert(0, r)            
            num = num // 10            
            
        return answer