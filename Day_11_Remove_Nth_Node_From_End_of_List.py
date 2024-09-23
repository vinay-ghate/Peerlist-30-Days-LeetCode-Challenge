# Challenge 11 — Remove Nth Node From End of List
# Problem: Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example: Input: head = [1,2,3,4,5], n = 2 Output: [1,2,3,5]

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
      
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
