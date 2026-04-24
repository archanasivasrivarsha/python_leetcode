Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def longestCommonPrefix(self, strs: list[str]) -> str:
...         if not strs:
...             return ""
...         
...         prefix = strs[0]
...         
...         for s in strs[1:]:
...             while not s.startswith(prefix):
...                 prefix = prefix[:-1]
...                 if prefix == "":
...                     return ""
...         
