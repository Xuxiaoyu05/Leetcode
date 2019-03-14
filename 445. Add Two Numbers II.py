# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7

# 不允许逆转链表

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2):
    # 用栈来实现
    stack1 = []
    stack2 = []
    add1 = 0
    
    dummy = ListNode(-1)
    dummy.next = None
    
    cur1, cur2 = l1, l2  
    
    while cur1:  # 可以直接用l1，l2
      stack1.append(cur1.val)
      cur1 = cur1.next
    
    while cur2:
      stack2.append(cur2.val)
      cur2 = cur2.next
    
    while stack1 or stack2:
      if stack1 and stack2:
        temp = stack1.pop() + stack2.pop() + add1
      elif stack1:
        temp = stack1.pop() + add1
      else:
        temp = stack2.pop() + add1
      
      node = ListNode(temp%10)  # 另一种写法，初始时令head=None, temp = head, head = ListNode(temp%10), head.next = temp, 最后return head
      add1 = temp // 10
      node.next = dummy.next
      dummy.next = node
    
    if add1 == 1:
      head = ListNode(1)
      head.next = dummy.next
      dummy.next = head
   
    return dummy.next
    
S = Solution()

node1 = ListNode(7)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4

node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(4)

node5.next = node6
node6.next = node7

print(S.addTwoNumbers(node1, node5).next.val)    
