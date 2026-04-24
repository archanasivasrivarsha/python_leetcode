Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        closest_sum = nums[0] + nums[1] + nums[2]
        
...         for i in range(n):
...             left, right = i + 1, n - 1
...             
...             while left < right:
...                 current_sum = nums[i] + nums[left] + nums[right]
...                 
...                 # Update closest sum
...                 if abs(current_sum - target) < abs(closest_sum - target):
...                     closest_sum = current_sum
...                 
...                 # Move pointers
...                 if current_sum < target:
...                     left += 1
...                 elif current_sum > target:
...                     right -= 1
...                 else:
...                     return current_sum  # exact match
...         
