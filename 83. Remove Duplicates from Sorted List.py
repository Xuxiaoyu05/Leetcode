# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# 输入: 1->1->2->3->3
# 输出: 1->2->3

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def deleteDuplicates(self, head):
    if not head:
      return
   
    record = [head.val]
    pre, cur = head, head.next
    
    while cur:
      if cur.val in record:
        pre.next = cur.next
      else:
        record.append(cur.val)
        pre = pre.next
      cur = cur.next
    
    return head
    
    
S = Solution()

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(S.deleteDuplicates(node1).next.val) 
