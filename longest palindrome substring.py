Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Solution:
    def longestPalindrome(self, s):
        def expand(left, right):
...             while left >= 0 and right < len(s) and s[left] == s[right]:
...                 left -= 1
...                 right += 1
...             return s[left+1:right]
... 
...         result = ""
... 
...         for i in range(len(s)):
...             # Odd length
...             temp1 = expand(i, i)
...             if len(temp1) > len(result):
...                 result = temp1
... 
...             # Even length
...             temp2 = expand(i, i+1)
...             if len(temp2) > len(result):
...                 result = temp2
... 
