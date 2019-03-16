# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。

# -*- coding:UTF-8 -*-
 
class Solution:
  def searchRange(self, nums, target):  
    left = 0
    right = len(nums) - 1

    while left <= right:
      mid = (left + right) // 2
      if target > nums[mid]:
        left = mid + 1 
      elif target < nums[mid]:
        right = mid - 1
      else:
        upper = self.upper(nums, target, mid+1, right)
        lower = self.lower(nums, target, left, mid-1)
        return [lower, upper]
     return [-1, -1]
   
   def upper(self, nums, target, left, right):
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] > target:
        right = mid - 1   
      else:
        left = mid + 1
    return right
  
   def lower(self, nums, target, left, right):
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] < target:     
        left = mid + 1
      else:
        right = mid - 1
    return left
 
 S = Solution()
 nums = [5,7,7,8,8,10]
 target = 8
 print(S.searchRange(nums, target))
