# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: 'ListNode | None', l2: 'ListNode | None') -> 'ListNode | None':
        dummy = ListNode(0)
        current = dummy
        carry = 0
        p, q = l1, l2
        while p or q or carry:
            val1 = p.val if p else 0
            val2 = q.val if q else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if p:
                p = p.next
            if q:
                q = q.next
        return dummy.next