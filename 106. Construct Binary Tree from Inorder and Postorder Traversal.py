# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 假设树中没有重复的元素


# -*- coding:UTF-8 -*-


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def buildTree(self, inorder, postorder):
    if not inorder or not postorder:
      return None
      
    root = TreeNode(postorder[-1])
    pos = inorder.index(postorder[-1])
    
    root.left = self.buildTree(inorder[:pos], postorder[:pos])
    root.right = self.buildTree(inorder[pos+1:], postorder[pos:-1])
    return root

S = Solution()
inorder = [9,3,15,20,7]    
postorder = [9,15,7,20,3]

print(S.buildTree(inorder, postorder))
