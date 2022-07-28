class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # DFS 방식
        def dfs(l, r):
            
            if not root:
                return True
            
            if not (l and not r):
                return True
            if not (l or not r):
                return False
            
            return l.val == r.val and dfs(l.left, r.right) and dfs(l.right, r.left)
        
        return dfs(root.left, root.right)
      
        # BFS 방식
        # q = collections.deque([root])

        # while q:
        #     level = []
        #     size = len(q)
        #     print(size)

        #     for i in range(size):
                
        #         node = q.popleft()
        #         if not node:
        #             level.append(None)
        #         else:
        #             level.append(node.val)
            
        #             q.append(node.left)
        #             q.append(node.right)
            
        #     print(level)
            
        #     if level != level[::-1]: return False
            
        # return True
