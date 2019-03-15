# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）

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
    
  def levelOrder(self, head):
    if not head:
      return []
    
    queue = []
    queue.append(head)
    res = []
    
    while queue:
      currentNode = queue.pop(0)
      res.append(currentNode.val)
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    return res
    

S = Solution()

alist = [1, [8, [2, [5], [6]], [7]], [9, [3], [4]]]

tree = S.createTree(alist)

print(S.levelOrder(tree))     
