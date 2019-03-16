# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 请找出其中最小的元素。
# 注意数组中可能存在重复的元素。

class Solution:
  def findMin(self, nums):
    left = 0
    right = len(nums) - 1
    
    while left < right and nums[left] >= nums[right]:
      mid = (left + right) // 2
      # mid 在第一个数组内
      if nums[mid] > nums[left]:
        left = mid + 1
      # mid 在第二个数组内
      elif nums[mid] < nums[left]:
        right = mid
      else:
        left += 1
       
    return nums[left]
    
S = Solution()
nums = [2,2,2,0,1]
print(S.findMin(nums))
