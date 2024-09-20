# Challenge 10 — Middle of the Linked List
# Problem: Given the head of a linked list, return the middle node. If there are two middle nodes, return the second middle node.

# Example: Input: head = [1,2,3,4,5] Output: [3,4,5]

# Method 1
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        temp = head
        while True:
            if head.next==None:
                return temp
            head = head.next
            cnt+=1
            if cnt%2==0:
                temp = temp.next

# Method 2
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        while head:
            list.append(head)
            head = head.next
        return list[len(list)//2]

# https://leetcode.com/problems/middle-of-the-linked-list/
