# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def deleteDuplicates(self, head):
    if not head:
      return 

    dummy = ListNode(-1)
    dummy.next = head
    pre, cur = dummy, head
    
    while cur:
      temp = cur.val
      count = 0
      
      while cur and cur.val == temp:
        cur = cur.next
        count += 1
      
      if count > 1:
        pre.next = cur
      else:
        pre = pre.next  # 此处无cur = cur.next
     
    return dummy.next
    
    
S = Solution()

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node6 = ListNode(4)
node7 = ListNode(4)
node8 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

print(S.deleteDuplicates(node1).next.val)
