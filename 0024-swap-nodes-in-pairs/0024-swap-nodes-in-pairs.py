# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, first = dummy, head

        while first and first.next:
            second = first.next
            third = first.next.next

            first.next = third
            second.next = first
            prev.next = second

            prev = first
            first = third

        return dummy.next
        