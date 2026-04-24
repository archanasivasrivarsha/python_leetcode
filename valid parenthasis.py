Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def isValid(self, s: str) -> bool:
...         stack = []
...         
...         mapping = {
...             ')': '(',
...             '}': '{',
...             ']': '['
...         }
...         
...         for ch in s:
...             if ch in mapping:  # closing bracket
...                 if not stack or stack[-1] != mapping[ch]:
...                     return False
...                 stack.pop()
...             else:  # opening bracket
...                 stack.append(ch)
...         
