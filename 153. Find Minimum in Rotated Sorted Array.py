# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 请找出其中最小的元素。
# 你可以假设数组中不存在重复元素。

class Solution:
  def findMin(self, nums):
    left = 0
    right = len(nums) - 1
    
    while left < right and nums[left] > nums[right]:
      mid = (left + right) // 2
      if nums[mid] >= nums[left]:
        left = mid + 1
      elif nums[mid] < nums[left]:   
        right = mid   # 注意：当mid在第二个数组时，right = mid，而不是mid-1，因为可能刚好处于最小值上
    return nums[left]
    
S = Solution()
nums = [4,5,6,7,0,1,2]
print(S.findMin(nums))
