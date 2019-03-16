# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。

# -*- coding:UTF-8 -*-

class Solution:
  def searchInsert(self, nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] > target:
        right = mid - 1
      else:
        left = mid + 1
    return left
    
S = Solution()
nums = [1,3,5,6]
target = 5
print(S.searchInsert(nums, target))
