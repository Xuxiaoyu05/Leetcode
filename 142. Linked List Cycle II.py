# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution:
  def detectCycle(self, head):
    if not head:
      return None
    
    slow, fast = head, head
    flag = False
    
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
        flag = True
        break
    
    if flag:
      fast = head
      while fast:
        if fast == slow:  # 注意：环有两种形式：（1）从头结点开始（2）从中途开始，因此应先判断是否相等，再移动，如[1,2]
          return fast
        fast = fast.next
        slow = slow.next
     return None
    
    
S = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

print(S.detectCycle(node1).val)     
