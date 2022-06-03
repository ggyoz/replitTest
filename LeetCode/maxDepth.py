# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        dep = 0
        res = []
        Solution.cntDepth(root, dep, res)
        
        return max(res)
        
    def cntDepth(root, dep, res):               
                
        if root != None:            
            dep += 1            
            Solution.cntDepth(root.left, dep, res)
            Solution.cntDepth(root.right, dep, res)
            
        else:
            res.append(dep)           
            
            
        
        
            
            
        
        
    
        
        
        