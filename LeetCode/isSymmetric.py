class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
      
        # BFS 방식
        q = collections.deque([root])

        while q:
            level = []
            size = len(q)
            print(size)

            for i in range(size):
                
                node = q.popleft()
                if not node:
                    level.append(None)
                else:
                    level.append(node.val)
            
                    q.append(node.left)
                    q.append(node.right)
            
            print(level)
            
            if level != level[::-1]: return False
            
        return True
