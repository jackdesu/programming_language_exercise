# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = current_node = ListNode(0)
        increase = 0
        while l1 is not None and l2 is not None:
            current_node.next = ListNode(l1.val + l2.val + increase)
            current_node = current_node.next
            if current_node.val > 9:
                current_node.val = current_node.val - 10
                increase = 1
            else:
                increase = 0

            if increase != 0 and l1.next is None and l2.next is None:
                l1.next = ListNode(increase)
                increase = 0

            l1 = l1.next
            l2 = l2.next

        if l1 is not None:
            current_node.next = l1
            while l1 is not None:
                l1.val += increase
                increase = 0
                if l1.val > 9:
                    increase = 1
                    l1.val -= 10

                if increase != 0 and l1.next is None:
                    l1.next = ListNode(increase)
                    increase = 0
                    break
                l1 = l1.next

        if l2 is not None:
            current_node.next = l2
            while l2 is not None:
                l2.val += increase
                increase = 0
                if l2.val > 9:
                    increase = 1
                    l2.val -= 10

                if increase != 0 and l2.next is None:
                    l2.next = ListNode(increase)
                    increase = 0
                    break
                l2 = l2.next

        return head.next