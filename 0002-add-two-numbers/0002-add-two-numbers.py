# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #build list of nums from l1 and l2
        list1 = []
        list2 = []

        while l1 != None:
            list1.insert(0,l1.val)
            l1 = l1.next
        while l2 != None:
            list2.insert(0,l2.val)
            l2 = l2.next

        num1 = ''
        num2 = ''

        for i in range(len(list1)):
            num1=num1+str(list1[i])
        for i in range(len(list2)):
            num2=num2+str(list2[i])

        #turn sum into int
        total = (int(num1)+int(num2))
        #init sum linked list

        head = ListNode()
        curr = head

        for digit in str(total)[::-1]:  # Digits of the sum in reverse order
            curr.next = ListNode(int(digit))  # Create and link a new node
            curr = curr.next  # Move to the newly created node

        return head.next
