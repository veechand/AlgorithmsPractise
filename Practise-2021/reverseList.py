
    def reverseList(self, head):
        curr = head
        prev = None
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev