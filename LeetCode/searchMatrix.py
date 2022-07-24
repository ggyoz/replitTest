class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # m == n 같을경우
      
        num = 0
        
        for a in range(len(matrix)):            
            if matrix[a][a] > target:
                num = a
                break
            elif matrix[a][a] == target:
                return True
        
        for i in range(num + 1):            
            if matrix[i][num] == target or matrix[num][i] == target:
                return True
                
        return False                    
       