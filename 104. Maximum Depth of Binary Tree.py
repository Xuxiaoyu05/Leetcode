# 给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

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
        
  # 迭代
  def maxDepth1(self, root):
    if not root:
      return 0
    return max(self.maxDepth1(root.left), self.maxDepth1(root.right)) + 1
  
  # 非迭代
  def maxDepth2(self, root):
    if not root:
      return 0
    
    queue = []
    queue.append(root)
    depth = 0
    
    while queue:
      childs = []
      for node in queue:
        if node.left:
          childs.append(node.left)
        if node.right:
          childs.append(node.right)
      queue = childs
      depth += 1
   
    return depth
 
 
S = Solution()

alist = [1, [8, [2, [5], [6]], [7]], [9, [3], [4]]]

tree = S.createTree(alist)

print(S.maxDepth1(tree))   
print(S.maxDepth2(tree))   
