class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def areMirrorImage(leftNode, rightNode):
            if (not (leftNode and not rightNode):
                return True
            if (not (leftNode or not rightNode):
                return False
            
            return leftNode.val == rightNode.val and areMirrorImage(leftNode.left, rightNode.right) and areMirrorImage(leftNode.right, rightNode.left)
        
        
        if not root:
            return True
        
        return areMirrorImage(root.left, root.right)