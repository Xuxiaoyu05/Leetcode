# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

# -*- coding:UTF-8 -*-

class Solution:
  def searchMatrix(self, matrix, target):
    if matrix == []:
      return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    i, j = 0, cols - 1
    
    while i < rows and j >= 0:    # 注意：不是 j < cols，因为j是自减的，不要粗心！！
      if target == matrix[i][j]:
        return True
      elif target > matrix[i][j]:
        i += 1
      else:
        j -= 1
    return False
    
S = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3

print(S.searchMatrix(matrix, target))
