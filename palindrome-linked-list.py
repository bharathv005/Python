class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        

        prev=None
        while slow:
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp

        left,right=head,prev
        while right:
            if left.val != right.val:
                return False
            right=right.next
            left=left.next
        return True
