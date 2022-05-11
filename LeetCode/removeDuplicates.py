class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # 연속된 문자 제거방법은 stack으로 풀면 빠름
        stack = []
        for c in s:

            # stack[-1] 가장 위에있는 값을 가져옴
            if stack and stack[-1][0] == c: 
                stack[-1][1] += 1
            else: 
                stack.append([c, 1])        
                
            if stack[-1][1] == k: 
                stack.pop()
        
        return "".join(x*c for x, c in stack)