# 旋转链表
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution:
  def rotateRight(self, head, k):
    if not head or k <= 0:
      return
    
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy
    
    
    
