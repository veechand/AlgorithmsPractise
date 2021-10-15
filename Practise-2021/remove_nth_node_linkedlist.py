"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Testcase
- Remove the first node
- Removing last node
- Node that's bigger than X

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
	def __init__(self):
		pass
	def remove_nth_node(self, head, n):
		ll_length = self.find_length(head)
		node_to_remove = ll_length - n
		return self.remove_nth_node_from_front(head, node_to_remove)
	def find_length(self, head):
		length = 0
		cur_head = head
		while cur_head != None:
			length += 1
			cur_head = cur_head.next
		return length
	def remove_nth_node_from_front(self, head, node_to_remove):
		if node_to_remove < 0:
			return head
		i = 1
		cur_head = head
		while i < node_to_remove:
			cur_head = cur_head.next
			i += 1
		if node_to_remove != 0:
			temp = cur_head.next
			cur_head.next = cur_head.next.next if cur_head.next != None else None
			temp.next = None
		else:
			head = head.next
		return head

	def print_node(self,node):
		while node != None:
			print node.val,
			node = node.next

if __name__ == "__main__":
	e_node = ListNode("E")
	d_node = ListNode("D", e_node)
	c_node = ListNode("C", d_node)
	b_node = ListNode("B", c_node)
	a_node = ListNode("A", b_node)
	solution = Solution()
	solution.print_node(a_node)
	head = solution.remove_nth_node(a_node, 9)
	print
	solution.print_node(head)
