class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head == None:
            return head
        elements = []
        cur = head
        elements.append(head.val)
        while cur.next != None:
            cur = cur.next
            elements.append(cur.val)
        newNode = ListNode()
        newNode.val = elements.pop(-1)
        elements.reverse()
        cursor = newNode
        for i in elements:
            cursor.next = ListNode(i)
            cursor = cursor.next
        return newNode