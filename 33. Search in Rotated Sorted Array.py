# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。

# -*- coding:UTF-8 -*-

class Solution:
  def search(self, nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        if nums[mid] < nums[left] and target >= nums[left]:
          right = mid - 1
        else:
          left = mid + 1
      else:
        if target < nums[left] and nums[mid] >= nums[left]:
          left = mid + 1
        else:
          right = mid - 1
     return -1
        
S = Solution()
nums = [4,5,6,7,0,1,2]
print(S.search(nums, 1))     
