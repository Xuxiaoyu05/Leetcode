# 请判断一个链表是否为回文链表。

# 输入: 1->2->2->1
# 输出: true

# -*- coding:UTF-8 -*-

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def isPalindrome(self, head):
    if not head:
      return False
    
    slow, fast = head, head.next
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    
    # 链表断开
    cur = slow.next
    slow.next = None
    
    while cur:
      temp = cur
      cur = cur.next
      temp.next = slow.next
      slow.next = temp
    
    # 再次断开
    second = slow.next
    slow.next = None
    
    while second:
      if head.val != second.val:  # 注意：此处需要比较的是值，而不是head != second（不是一个结点），否则会一直返回False
        return False
      head = head.next
      second = second.next
    return True


S = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

print(S.isPalindrome(node1))
