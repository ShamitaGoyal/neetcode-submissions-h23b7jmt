# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head 
        fast = head 

        # make sure fast isnt already at None
        #and make sure fast.next can take a second step without crashing
        #if either is None, this list ended, so no cycle 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                return True 

        return False
        