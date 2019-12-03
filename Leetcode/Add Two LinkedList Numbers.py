# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    l1_size = 0
    l2_size = 0

    l1_current = l1
    while l1_current:
        l1_size += 1
        l1_current = l1_current.next

    l2_current = l2
    while l2_current:
        l2_size += 1
        l2_current = l2_current.next

    carry = 0
    result = ListNode(0)
    if l1_size >= l2_size:
        l1_current = l1
        l2_current = l2
        while l1_current:
            temp = l1_current.val + l2_current.val + carry
            carry = temp % 10
            if carry == 0:
                result.val = temp
                result = result.next
            else:
                result.val = carry
                result = result.next
            l2_current = l2_current.next
            l1_current = l1_current.next



if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    addTwoNumbers(l1, l2)
