# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        mergelist = dummy = ListNode()               
        
        while list1 and list2:
            
            if list1.val <= list2.val:                    
                mergelist.next = ListNode(list1.val)
                list1 = list1.next
            else:                    
                mergelist.next = ListNode(list2.val)                
                list2 = list2.next            
                
            mergelist = mergelist.next
            
        if list1 == None:
            mergelist.next = list2
        else:
            mergelist.next = list1            
            
        return dummy.next