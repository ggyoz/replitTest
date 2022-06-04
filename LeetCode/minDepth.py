# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:        
        
        res = []
        dep = 0
        Solution.cntMin(root, dep, res)
        
        if len(res) == 0:
            res.append(0)

        return min(res)
        
    def cntMin(root, dep, res):        
        
        if root:
            dep += 1            
            
            if root.right == None and root.left == None:
                res.append(dep)
            
            Solution.cntMin(root.right, dep, res)
            Solution.cntMin(root.left, dep, res)                      
            