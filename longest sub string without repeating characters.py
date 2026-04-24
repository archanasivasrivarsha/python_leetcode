Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def lengthOfLongestSubstring(self, s):
...         char_set = set()
...         left = 0
...         max_length = 0
... 
...         for right in range(len(s)):
...             while s[right] in char_set:
...                 char_set.remove(s[left])
...                 left += 1
... 
...             char_set.add(s[right])
...             max_length = max(max_length, right - left + 1)
... 
