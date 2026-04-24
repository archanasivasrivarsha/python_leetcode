Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def convert(self, s, numRows):
...         if numRows == 1 or numRows >= len(s):
...             return s
... 
...         rows = [""] * numRows
...         cur_row = 0
...         going_down = False
... 
...         for char in s:
...             rows[cur_row] += char
... 
...             # Change direction
...             if cur_row == 0 or cur_row == numRows - 1:
...                 going_down = not going_down
... 
...             cur_row += 1 if going_down else -1
... 
