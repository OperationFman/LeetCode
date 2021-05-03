class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head): #Note: Replacing the original LL wouldn't accept despite it being correct
        """ ListNode{val: 1, next: ListNode{val: 2, 
            next: ListNode{val: 3, next: ListNode{val: 4, 
            next: ListNode{val: 5, next: None}}}}} """
        if head == None or head.next == None: # head or next could be nothing
            return head # The reverse of None is None and a single number would just be... that number
        
        cur = head # Set a cursor instance
        array = [] # Empty list to store the LL, much easier to reverse this than a LL
        array.append(cur.val) # Add the first value manually so we only worry about cur.next when moving through the list
        
        while cur.next != None: # If cur.next is None we've reached the end of the list
            cur = cur.next # 2. Make cur the next value since we'd already added the first val
            array.append(cur.val) # 1. Add the value of cur to the list
            # These are flipped because for some reason the last value doesn;t get grabbed
            
        array.reverse()
        newList = ListNode() # Create a new instance of a Linked List
        cur = newList # Create a cursor on the start of it
        cur.val = array.pop(0) # Similar to reading, manually set the first val so we only worry about next
            
        for i in array: # using the array since when it ends, we're done
            cur.next = ListNode() # Create a new empty node on the next of the cursor
            cur.next.val = i # make the next value whatever we're upto in the array
            cur = cur.next # move down the linked list so next is now None
            
        return newList 
        # ListNode{val: 5, next: 
        #   ListNode{val: 4, next: 
        #       ListNode{val: 3, next:
        #           ListNode{val: 2, next: 
        #               ListNode{val: 1, next: 
        #                   None}}}}}