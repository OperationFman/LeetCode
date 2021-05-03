class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head): #Note: Replacing the original LL wouldn't accept despite it being correct
        """ ListNode{val: 1, next: ListNode{val: 2, 
            next: ListNode{val: 3, next: ListNode{val: 4, 
            next: ListNode{val: 5, next: None}}}}} """
        if head == None or head.next == None:
            return head
        
        cur = head
        array = []
        array.append(cur.val)
        
        while cur.next != None:
            cur = cur.next
            array.append(cur.val)
            
        array.reverse()
        newList = ListNode()
        cur = newList
        cur.val = array.pop(0)
            
        for i in array:
            cur.next = ListNode()
            cur.next.val = i
            cur = cur.next
            
        return newList