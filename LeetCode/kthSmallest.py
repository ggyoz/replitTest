class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        a = list()
        
        for m in matrix:
            a += m
        
        a.sort()
        
        return a[k-1]
