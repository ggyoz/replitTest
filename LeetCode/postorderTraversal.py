# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        tree = []
        
        def dfs(root):
            
            if root and root.val:        
                l = dfs(root.left)
                if l:
                    tree.append(l)
                r = dfs(root.right)                
                if r:
                    tree.append(r)               
                return root.val

        t = dfs(root)
        if t:        
            tree.append(t)
                
        return tree