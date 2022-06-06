# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        visited = []
        calc = 0                
        
        def dfs(root, calc, visited):
            
            if targetSum in visited:
                return
            
            if root:

                calc += root.val
                dfs(root.left, calc, visited)
                dfs(root.right, calc, visited)

                if not root.left and not root.right:
                    visited.append(calc)
            else:
                return
            
         
        dfs(root, calc, visited)        
        
        if targetSum in visited:
            return True
        else:
            return False
            