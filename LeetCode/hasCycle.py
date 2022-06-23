class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        
        # FLOYD TORTOISE ALGORITHM(토끼와 거북이 알고리즘) 사용
        slow, fast = head, head
        
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
          
            # slow와 fast가 같으면 Cycle가 존재함
            if fast == slow:
                return True
            
        return False       
        