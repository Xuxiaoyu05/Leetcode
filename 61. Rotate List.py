# 旋转链表
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution:
  def rotateRight(self, head, k):
    if not head or k <= 0:
      return
    
    length = 1
    cur = head
    while cur.next:
      cur = cur.next
      length += 1
    
    cur.next = head  # 首尾相连
   
    gap = length - k % length    # 判断需要移动的次数
    
    # cur = head   # 并不需要这一步，cur还是位于初始的尾结点
    
    # 寻找待断开的前驱
    while gap != 0:  
      cur = cur.next  
      gap -= 1
    
    head = cur.next  # 注意：此句话要加上
    cur.next = None  # 将环链断开
    
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

print(S.rotateRight(node1, 2).next.val)
