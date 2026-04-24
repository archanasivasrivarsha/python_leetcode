Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n):
            # Skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n):
                # Skip duplicate j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
...                         result.append([nums[i], nums[j], nums[left], nums[right]])
...                         
...                         # Skip duplicates for left
...                         while left < right and nums[left] == nums[left + 1]:
...                             left += 1
...                         
...                         # Skip duplicates for right
...                         while left < right and nums[right] == nums[right - 1]:
...                             right -= 1
...                         
...                         left += 1
...                         right -= 1
...                     
...                     elif total < target:
...                         left += 1
...                     else:
...                         right -= 1
...         
