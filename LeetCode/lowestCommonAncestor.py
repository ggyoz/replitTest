# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            
#         print(p)
        
#         if root in (None, p, q):
#             print(True)
#         else:
#             print(False)        
        
        if root == None or root == p or root == q:
            return root        
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)        
        
        if left != None and right != None:
            print('root.val',root.val)
            return root
        elif left != None:
            print('left',left)
            return left
        elif right != None:
            print('right',right)
            return right
        
        
        
        
        