# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        p_list = []
        q_list = []        
        
        Solution.addArray(p, p_list)        
        Solution.addArray(q, q_list)
        
        print(p_list)
        print(q_list)
        
        
        return p_list == q_list
        
    
    def addArray(root: Optional[TreeNode], answer: list):          
        
        if root == None:
            return
        
        Solution.addArray(root.left, answer)        
        answer.append(root.val)        
        Solution.addArray(root.right, answer)        
        
        
        
        