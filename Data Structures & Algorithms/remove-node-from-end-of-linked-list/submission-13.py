class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        savehead = head
        idx = 0
        while head.next:
            head = head.next
            idx += 1
        length = idx + 1  # total number of nodes

        # if removing the head itself
        if n == length:
            return savehead.next

        # steps to reach the PREDECESSOR of the target node
        traverse = length - n - 1

        head = savehead
        for _ in range(traverse):
            head = head.next

        head.next = head.next.next
        return savehead