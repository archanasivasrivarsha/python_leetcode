Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def twoSum(self, nums, target):
...         num_map = {}  # value -> index
... 
...         for i in range(len(nums)):
...             complement = target - nums[i]
... 
...             if complement in num_map:
...                 return [num_map[complement], i]
... 
