from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
def print_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
    

if __name__ == "__main__":
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    sol = Solution()
    reversed_head = sol.reverseList(node1)

    print("Reversed list:")
    print_list(reversed_head)