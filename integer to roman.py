Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
...             1000, 900, 500, 400,
...             100, 90, 50, 40,
...             10, 9, 5, 4, 1
...         ]
...         
...         symbols = [
...             "M", "CM", "D", "CD",
...             "C", "XC", "L", "XL",
...             "X", "IX", "V", "IV", "I"
...         ]
...         
...         result = ""
...         
...         for i in range(len(values)):
...             while num >= values[i]:
...                 result += symbols[i]
...                 num -= values[i]
...         
