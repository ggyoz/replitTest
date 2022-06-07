class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = [[1 for j in range(0, i)] for i in range(1, numRows + 1)]        
        
        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
                
        return result