class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node=None
        prev=None
        curr=head
        while curr:
            new_node=curr.next
            curr.next=prev
            prev=curr
            curr=new_node
        return prev