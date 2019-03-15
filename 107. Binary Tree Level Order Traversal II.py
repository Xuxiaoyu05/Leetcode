# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）


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
  
  def levelOrderBottom(self, root):
    if not root:
      return []
    
    queue = []
    queue.append(root)
    res = []
    
    while queue:
      childs = []
      temp = []
      for node in queue:
        temp.append(node.val)
        if node.left:
          childs.append(node.left)
        if node.right:
          childs.append(node.right)
      queue = childs
      res.insert(0, temp)
    return res
    

S = Solution()

alist = [1, [8, [2, [5], [6]], [7]], [9, [3], [4]]]

tree = S.createTree(alist)

print(S.levelOrderBottom(tree))   
