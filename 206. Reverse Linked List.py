# 反转一个单链表。
# 示例: 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # 递归
  def reverseList1(self, head):
    if not head or not head.next: 
      return head
      
    pHead = self.reverseList1(head.next)
    head.next.next = head
    head.next = None
    return pHead
    
 
 # 非递归1：新建链表
  def reverseList2(self, head):
    dummy = ListNode(-1)
    dummy.next = None
    cur = head
    
    while cur:
      temp = cur
      cur = cur.next
      temp.next = dummy.next
      dummy.next = temp
    return dummy.next
   
   # 非递归2：原地实现摘链和链接
   def reverseList3(self, head):
    if not head:
      return head
    
    dummy = ListNode(-1)
    dummy.next = head

    pre, cur = head, head.next
    
    while cur:  # 注意：
      temp = cur
      pre.next = cur.next
      cur = pre.next
      temp.next = dummy.next
      dummy.next = temp
     
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
node4.next = node5

print(S.reverseList3(node1).val)    
