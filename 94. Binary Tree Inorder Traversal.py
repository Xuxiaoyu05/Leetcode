# 给定一个二叉树，返回它的中序 遍历。

# -*- coding:UTF-8 -*-

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def createTree(self, alist):
    if alist == []:
      return None
    
    root = TreeNode(alist[0])
    if len(alist) >= 2:
      root.left = self.createTree(alist[1])
    if len(alist) >= 3:
      root.right = self.createTree(alist[2])
    
    return root   # 注意：此处一定要返回root，否则tree为空呀！！！
   
  def inOrder(self, root):
    if not root:
      return 
      
    res = []
    stack = []
    currentNode = root
    
    while currentNode or len(stack) > 0:
      # 一直向左深入，存入栈中
      if currentNode:
        stack.append(currentNode)
        currentNode = currentNode.left
      else:
        currentNode = stack.pop()
        res.append(currentNode.val)
        currentNode = currentNode.right
        
     return res
   
S = Solution()
alist = [1, [8, [2, [5], [6]], [7]], [9, [3], [4]]]
tree = S.createTree(alist)
print(S.inOrder(tree))
