# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            currlist = []
            # currlist = self.mergelist(lists[0], lists[1])
            # lists = [currlist] + lists[2:]
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                currlist.append(self.mergelist(l1,l2))
            lists = currlist
        return lists[0]
    
    def mergelist(self, list1, list2):
        finallist = ListNode()
        head = finallist

        while list1 and list2:
            if list1.val <= list2.val:
                finallist.next = list1
                finallist = finallist.next
                list1 = list1.next
            else:
                finallist.next = list2
                finallist = finallist.next
                list2 = list2.next 

        if list1:
            finallist.next = list1
        if list2:
            finallist.next = list2
        return head.next
    
