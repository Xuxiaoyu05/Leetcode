# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution:
  def middleNode(self, head):
    slow, fast = head, head
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    
    return slow
    
S = Solution()

node1 = ListNode(7)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4

print(S.middleNode(node1).val)
