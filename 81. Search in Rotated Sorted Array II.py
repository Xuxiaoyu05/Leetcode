# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
# 可能有重复元素

# -*- coding:UTF-8 -*-

class Solution:
  def search(self, nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
      mid = (left + right) // 2
      if target == nums[mid]:
        return True
      elif nums[mid] > nums[left]:
        if target < nums[mid] and target >= nums[left]:
          right = mid - 1
        else:
          left = mid + 1  
      elif nums[mid] < nums[left]:
        if target > nums[mid] and target <= nums[right]:  # 注意：此处是target <= nums[right]而不是left，因为限定在mid的右边
          left = mid + 1
        else:  
          right = mid - 1
      else:
        left += 1
    return False
 

S = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print(S.search(nums, target))     
