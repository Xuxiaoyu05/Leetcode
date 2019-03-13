# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

# -*- coding;UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def reorderList(self, head):
    if not head:
      return
    
    slow, fast = head, head.next
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    
    # 将链表断开
    cur = slow.next
    slow.next = None
    
    # 第二部分链表逆置
    while cur:
      temp = cur
      cur = cur.next
      temp.next = slow.next
      slow.next = temp
    
    # 将链表再次断开，插入
    cur = slow.next
    slow.next = None
    pre = head
    
    while cur:
      temp = cur
      cur = cur.next
      temp.next = pre.next
      pre.next = temp
      pre = temp.next
    return head
      
S = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(S.reorderList(node1).next.next.next.next.val)  
