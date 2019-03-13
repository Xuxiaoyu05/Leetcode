# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def removeNthFromEnd(self, head, n):
    if not head or n <= 0:
      return None
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy
    slow, fast = head, head
    for i in range(n):
      if fast:
        fast = fast.next
      else:
        return None
    
    while fast:
      fast = fast.next
      slow = slow.next   # 此时slow走到倒数第k个结点
      pre = pre.next
   
    pre.next = slow.next
    
    return dummy.next
    
    
S = Solution()
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
print(S.removeNthFromEnd(node1, 3).next.next.next.val)
