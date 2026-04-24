Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # starting node
...         current = dummy
...         carry = 0
... 
...         while l1 or l2 or carry:
...             val1 = l1.val if l1 else 0
...             val2 = l2.val if l2 else 0
... 
...             total = val1 + val2 + carry
...             carry = total // 10
... 
...             current.next = ListNode(total % 10)
...             current = current.next
... 
...             if l1:
...                 l1 = l1.next
...             if l2:
...                 l2 = l2.next
... 
