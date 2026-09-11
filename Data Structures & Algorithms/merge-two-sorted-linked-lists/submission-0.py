# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        nlist = dummy
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                nlist.next = list1
                list1 = list1.next
            else:
                nlist.next = list2
                list2 = list2.next
            nlist = nlist.next
        if list1 != None:
            nlist.next = list1
        elif list2 != None:
            nlist.next = list2
        return dummy.next