# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

# 输入: head = [4,5,1,9], node = 5
# 输出: [4,1,9]

class ListNode:
  def __init__(self, x):  
    self.val = x
    self.next = None
    
class Solution:
  def deleteNode(self, head, node):
    # node 非末尾结点，直接跳过即可
    node.val = node.next.val
    node.next = node.next.next
    return head
    
S = Solution()

node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4

print(S.deleteNode(node1, node2).next.val)
