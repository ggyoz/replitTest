# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if head == None:
            return
            
        curr = dummy = ListNode(head.val)        
        
        while head:
            
            print("h:", head.val)
            print("c:", curr.val)
            
            if head.val != curr.val:
                
                print(ListNode(head.val))
                
                curr.next = ListNode(head.val)
                curr = curr.next
                print("curr:", curr)
                print("dummy:", dummy)
                
            head = head.next
            
            
        print("dummy:", dummy)
        return dummy
            
            
            