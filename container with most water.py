Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def maxArea(self, height: list[int]) -> int:
...         left, right = 0, len(height) - 1
...         max_area = 0
...         
...         while left < right:
...             h = min(height[left], height[right])
...             w = right - left
...             max_area = max(max_area, h * w)
...             
...             # Move the smaller height pointer
...             if height[left] < height[right]:
...                 left += 1
...             else:
...                 right -= 1
...         
