# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head.next == None or left == right:
            return head
        
        l1 = head
        a1 = []
        
        index = 0               
        reverselist = dummy = ListNode()
                
        while l1:
            a1.append(l1.val)            
            l1 = l1.next
            
        a2 = a1[left-1:right:1][::-1]
        
        #print(a2)
        
        while head:
            
            if index >= left - 1 and index <= right - 1:                
                #print(index)
                #print(ListNode(a1[index]))
                #print(ListNode(a2.pop(0)))
                dummy.next = ListNode(a2.pop(0))
            else:
                dummy.next = head
                
            dummy = dummy.next            
            index += 1
            head = head.next
                        
        return reverselist.next
