# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 假设树中没有重复的元素

# -*- coding:UTF-8 -*-

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def buildTree(self, preorder, inorder):
    if not preorder or not inorder:
      return None
      
    root = TreeNode(preorder[0])
    pos = inorder.index(preorder[0])
    
    root.left = self.buildTree(preorder[1:pos+1], inorder[:pos])
    root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
    return root
    
S = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(S.buildTree(preorder, inorder))
