# 链表求和

# 给出两个 非空 的链表用来表示两个非负的整数。
# 其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution:
  def addTwoNumbers(self, l1, l2):   
    dummy = ListNode(-1)  # 新建一个链表
    pre = dummy

    cur1, cur2 = l1, l2
    add1 = 0
   
    while cur1 or cur2:
      if cur1 and cur2:
        temp = cur1.val + cur2.val + add1
        cur1 = cur1.next
        cur2 = cur2.next
      elif cur1:
        temp = cur1.val + add1
        cur1 = cur1.next
      else:
        temp = cur2.val + add1
        cur2 = cur2.val
      
      add1 = temp // 10
      node = ListNode(temp % 10)
      pre.next = node
      pre = pre.next
      
    return dummy.next

S = Solution()

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

print(S.addTwoNumbers(node1, node4).val)
