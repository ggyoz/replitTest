class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        result = [[1 for j in range(0,i)] for i in range(1, rowIndex + 2)]
        
        for a in range(2, rowIndex + 1):
            for b in range(1, a):
                result[a][b] = result[a - 1][b - 1] + result[a - 1][b]
                
        return result[rowIndex]