# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。

# -*- coding:UTF-8 -*-

class Solution:
  def searchMatrix(self, matrix, target):
    if matrix == []:
      return False
      
    rows = len(matrix)
    cols = len(matrix[0])
    
    i, j = 0, cols - 1
    
    while i < rows and j >= 0:
      if matrix[i][j] == target:
        return True
      elif target > matrix[i][j]:
        i += 1
      else:
        j -= 1
    return False
    
S = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
print(S.searchMatrix(matrix, target))
