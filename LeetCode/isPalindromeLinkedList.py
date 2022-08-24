# 234. Palindrome Linked List
# 주어진 singly-linked list가 회문인지 확인


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # 값 저장용 배열
        a = []        

        # linked list에서 값 추출
        while head:            
            a.append(head.val)            
            head = head.next        

        # 역순과 비교
        if a == a[::-1]:
            return True
        else:
            return False
        
            
            