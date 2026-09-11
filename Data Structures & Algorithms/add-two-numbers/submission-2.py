# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # finalnode = ListNode()
        # head = finalnode
        # while l1 and l2:
        #     nvalue = list(str(l1.val + l2.val))[::-1]
        #     for n in nvalue:
        #         finalnode.next = ListNode(int(n), None)
        #         finalnode = finalnode.next
        #     l1 = l1.next
        #     l2 = l2.next
        # return head.next
        n1 = ""
        while l1:
            n1 = str(l1.val) + n1
            l1 = l1.next
        
        n2 = ""
        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next


        final = list(str(int(n1) + int (n2)))[::-1]
        finalnode = ListNode()
        head = finalnode
        for val in final:
            finalnode.next = ListNode(val, None)
            finalnode = finalnode.next
        return head.next
