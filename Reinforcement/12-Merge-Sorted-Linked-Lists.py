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
            
            array1 = []
            array2 = []

            cur = l1

            array1.append(cur.val)
            while cur.next != None:
                array1.append(cur.next.val)
                cur = cur.next

            cur = l2
            array2.append(cur.val)
            while cur.next != None:
                array2.append(cur.next.val)
                cur = cur.next

            result = sorted(array1 + array2)

            newList = ListNode()
            cur = newList
            cur.val = result.pop(0)

            for i in result:
                cur.next = ListNode()
                cur.next.val = i
                cur = cur.next

            return newList
        except:
            node = ListNode()
            return node