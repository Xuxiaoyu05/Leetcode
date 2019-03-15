# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）

# -*- coding:UTF-8 -*-

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
    
class Solution:
  def createTree(self, alist):
        lens = len(alist)
        if lens == 0:
            return None
        root = TreeNode(alist[0])
        if lens >= 2:
            root.left = self.createTree(alist[1])
        if lens >= 3:
            root.right = self.createTree(alist[2])
        return root
        
  def zigzagLevelOrder(self, root):
    if not root:
      return []
    
    queue = []
    queue.append(root)
    res = []
    flag = True
    
    while queue:
      childs = []
      level = []
      for node in queue:
        level.append(node.val)
        if node.left:
          childs.append(node.left)
        if node.right:
          childs.append(node.right)
          
       if flag:
        res.append(level)
       else:
        level.reverse()
        res.append(level)
      flag = not flag
      
      queue = childs
    return res
    
S = Solution()

alist = [1, [8, [2, [5], [6]], [7]], [9, [3], [4]]]

tree = S.createTree(alist)

print(S.zigzagLevelOrder(tree))   
