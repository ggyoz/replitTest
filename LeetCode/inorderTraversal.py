# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        
        rootNode = root
        Solution.addArray(rootNode, answer)            
        
        return answer
    
# 재귀함수 사용        
    def addArray(root: Optional[TreeNode], answer: list):
        
        if root == None: return
        
        Solution.addArray(root.left, answer)
        
        answer.append(root.val)
        
        Solution.addArray(root.right, answer)        
            
        