# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # first step -> find the middle 

        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        

        #second step -> use the other half, reverse it 
        second = slow.next #Node4
        slow.next = None 
        prev = None 

        while second:
            tmp = second.next #Node 5
            second.next = prev # Node4 -> None 
            prev = second
            second = tmp
        second = prev 


        #third step -> merge the two halves 

        first = head 
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



        