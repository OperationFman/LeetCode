class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        """ [1,2,4] & [1,3,4] """
        try:
            if l1 == None and l2 == None: # If both inputs are nothing, return nothing
                return None
            elif l1 == None and l2 != None: # if one is nothing but the other isn't then the other would be the result anyway, might aswell just return it
                return l2
            elif l1 != None and l2 == None:
                return l1
            
            array1 = [] # Using arrays as it's easier to sort
            array2 = [] # Also easier to just fill them, then iterate over them making a new Linkedlist

            cur = l1 # Cursor to start at l1

            array1.append(cur.val) # First element gets skipped because we only use the 'next' value, so here we add it manually
            while cur.next != None: # Loop stops at the end of the LL
                array1.append(cur.next.val) # Put the value of next in the array and move down the LL
                cur = cur.next

            cur = l2 # Does exactly the same as previous block on the second array
            array2.append(cur.val)
            while cur.next != None:
                array2.append(cur.next.val)
                cur = cur.next

            result = sorted(array1 + array2) # Much easier and more readable to sort arrays this way and store as a new array

            newList = ListNode() # new instance of a linkedlist
            cur = newList
            cur.val = result.pop(0) # Similar to reading the LLs, the first would be missed to we add it manually. Also, by popping we can iterate over the remaining array easily

            for i in result:
                cur.next = ListNode() # Create a node and add it to the next
                cur.next.val = i # Change the values of said node
                cur = cur.next # Move down the LL

            return newList 
        except:
            node = ListNode() # Likely if something went wrong it was because it's an empty node, right after the try we catch 'nothing' but not a node with nothing
            return node # Two empty nodes would equal an empty node so might aswell catch and return it