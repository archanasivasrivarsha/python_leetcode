Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
...         dummy = ListNode(0)
...         dummy.next = head
...         
...         fast = dummy
...         slow = dummy
...         
...         # Move fast n+1 steps ahead
...         for _ in range(n + 1):
...             fast = fast.next
...         
...         # Move both pointers
...         while fast:
...             fast = fast.next
...             slow = slow.next
...         
...         # Remove nth node
...         slow.next = slow.next.next
...         
