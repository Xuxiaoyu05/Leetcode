# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 给定 1->2->3->4, 你应该返回 2->1->4->3.

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution:
  def swapPairs(self, head):
    if not head:
      return
      
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy    # 始终指向待交换结点的前驱
    first = head
    second = head.next
    
    while second:
      first.next = second.next
      second.next = first
      pre.next = second
      pre = first
      first = first.next
      second = first.next if first else None
      
    return dummy.next
    
    
S = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

print(S.swapPairs(node1).val)    
