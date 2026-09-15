# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#time complexity O(n)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #make dummy node
        dummy = ListNode(0,head)
        slow = fast = dummy 


        #1. make gap 
        for _ in range(n + 1):
            fast = fast.next 

        
        #2. make the slow pointer start 
        while fast:
            slow = slow.next 
            fast = fast.next 

        
        #3. delete the node -> relink 
        slow.next = slow.next.next 
        return dummy.next 