# 删除链表中等于给定值 val 的所有节点。

# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def removeElements(self, head, val):
    if not head:
      return
    
    dummy = ListNode(-1)
    dummy.next = head
    pre, cur = dummy, head
    
    while cur:
      if cur.val == val:
        pre.next = cur.next
      else:
        pre = pre.next
      cur = cur.next
    return dummy.next

S = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

print(S.removeElements(node1, 6).next.next.next.val)
