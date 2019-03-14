# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 说明: 1 ≤ m ≤ n ≤ 链表长度。
# 示例: 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
   def reverseBetween(self, head, m, n):
      dummy = ListNode(-1)
      dummy.next = head
      pre = dummy
      count = 1
      
      while count != m:
        pre = pre.next
        count += 1
      
      second = pre.next
      tail = second  # tail 记录翻转的起始元素，也是翻转部分翻转后的最后一个元素
      pre.next = None
      
      gap = n - m + 1
      while gap != 0:
        temp = second
        second = second.next
        temp.next = pre.next
        pre.next = temp
        gap -= 1
        
      tail.next = second
      return dummy.next
   
S = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node5.next = node5

print(S.reverseBetween(node1,2 , 4).next.val)      
