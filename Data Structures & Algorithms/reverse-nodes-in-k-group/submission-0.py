class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy  # tail of the previous (already processed) part

        while True:
            # 1. Check that k nodes remain
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # fewer than k left: leave as is
            group_next = kth.next

            # 2. Reverse the k nodes
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 3. Reconnect: the old first node is now the group's tail
            old_first = group_prev.next
            group_prev.next = kth   # kth is the new head of this group
            group_prev = old_first  # move on to the next group