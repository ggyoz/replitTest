# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
#     def dfs(self, copy):
        
#         if copy == None:
#             return copy
        
#         r = self.dfs(copy.right)
#         l = self.dfs(copy.left)        
        
#         if l == None and r == None:            
#             return copy

#         if r != None:            
#             if l != None:
#                 l.right = r
#                 return copy 
#             else: 
#                 return copy
#         else:
#             if l != None:
#                 copy.right = l
#                 return copy            
            
        def dfs(root):
            if not root: return None
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            if l:
                print('0', l)
                print('1', root.right)
                l.right = root.right
                print('2', root.left)
                root.right = root.left                
                root.left = None
            
            return r or l or root
        
        return dfs(root)
        