Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def isPalindrome(self, x: int) -> bool:
...         # Negative numbers are not palindrome
...         if x < 0 or (x % 10 == 0 and x != 0):
...             return False
...         
...         reversed_half = 0
...         
...         # Reverse half of the number
...         while x > reversed_half:
...             reversed_half = reversed_half * 10 + x % 10
...             x //= 10
...         
...         # For even digits: x == reversed_half
...         # For odd digits: x == reversed_half // 10
