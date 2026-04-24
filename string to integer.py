Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # Skip whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
...                 sign = -1
...             i += 1
...         
...         # Convert digits
...         num = 0
...         INT_MAX = 2**31 - 1
...         INT_MIN = -2**31
...         
...         while i < n and s[i].isdigit():
...             digit = int(s[i])
...             
...             # Overflow check
...             if num > (INT_MAX - digit) // 10:
...                 return INT_MAX if sign == 1 else INT_MIN
...             
...             num = num * 10 + digit
...             i += 1
...         
