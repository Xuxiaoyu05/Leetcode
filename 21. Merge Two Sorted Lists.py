# 合并两个有序链表
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的，满足单调不减原则。 

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def mergeTwoLists(self, l1, l2):
    dummy = ListNode(-1)
    dummy.next = l1
    pre = dummy
    
    cur1, cur2 = l1, l2
    
    while cur1 and cur2:
      if cur1.val > cur2.val:
        temp = cur2
        cur2 = cur2.next
        temp.next = cur1
        pre.next = temp
        pre = pre.next
      else:
        pre = pre.next
        cur1 = cur1.next
    
    return dummy.next
    
    
S = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

print(S.mergeTwoLists(node1, node4).next.next.next.val)
 
