# 给定一个链表，判断链表中是否有环

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def hasCycle(self, head):
    if not head:
      return False
    
    slow, fast = head, head
    
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
        return True
        
    return False
    
S = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(S.hasCycle(node1))   
