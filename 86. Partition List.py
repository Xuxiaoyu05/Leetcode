# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。
# 示例: 输入: head = 1->4->3->2->5->2, x = 3  # 输出: 1->2->2->4->3->5

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
   def partition(self, head, x):
      # 拆分成两个链表
      first = ListNode(-1)
      second = ListNode(-1)
      cur1, cur2 = first, second
      while head:
        if head.val < x:
          cur1.next = head
          head = head.next
          cur1 = cur1.next
        else:
          cur2.next = head
          head = head.next
          cur2 = cur2.next
          
       cur1.next = second.next
       cur2.next = None
       return first.next
          
S = Solution()

node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(S.partition(node1, 3).next.next.next.val)         
