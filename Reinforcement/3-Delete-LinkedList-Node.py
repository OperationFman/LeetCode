class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node): # We only know the node to delete, not the previous node
        """ ListNode{val: 5, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}} """
        while node.next.next != None: # Checks if the node 2 away exist, if the do
            node.val = node.next.val # Current equals next
            node = node.next # make the next node the current, while loop runs again if next.next isnt None
        # Loop breaks at the 2 last nodes in the Linked List, no more next.next

        node.val = node.next.val # Make the current the next one last time
        # Now the second last and last are the same
        node.next = None # Make the last None, ending the List