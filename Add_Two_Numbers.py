from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            a = ''
            while l1:
                s = ''.join(str(l1))
                l1 = l1
                break
            print(a)

Solution().addTwoNumbers([2,4,3], [5,6,4])