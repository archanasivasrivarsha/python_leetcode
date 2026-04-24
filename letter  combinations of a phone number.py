Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def letterCombinations(self, digits: str) -> list[str]:
...         if not digits:
...             return []
...         
...         phone = {
...             '2': 'abc', '3': 'def', '4': 'ghi',
...             '5': 'jkl', '6': 'mno', '7': 'pqrs',
...             '8': 'tuv', '9': 'wxyz'
...         }
...         
...         result = []
...         
...         def backtrack(index, path):
...             # If combination is complete
...             if index == len(digits):
...                 result.append(path)
                return
            
            # Get letters for current digit
            letters = phone[digits[index]]
            
            for ch in letters:
                backtrack(index + 1, path + ch)
        
        backtrack(0, "")
