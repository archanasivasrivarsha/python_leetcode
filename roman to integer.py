Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def romanToInt(self, s: str) -> int:
...         values = {
...             'I': 1, 'V': 5, 'X': 10, 'L': 50,
...             'C': 100, 'D': 500, 'M': 1000
...         }
...         
...         total = 0
...         
...         for i in range(len(s)):
...             # If next value is greater → subtract
...             if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
...                 total -= values[s[i]]
...             else:
...                 total += values[s[i]]
...         
