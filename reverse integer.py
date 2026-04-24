Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def reverse(self, x):
...         sign = -1 if x < 0 else 1
...         x = abs(x)
... 
...         rev = int(str(x)[::-1])
... 
...         if rev > 2**31 - 1:
...             return 0
... 
