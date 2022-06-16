# Url: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
 
# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        
        last_node = head
        new_head = last_node
        head = head.next
        
        while head:
            
            if last_node.val == head.val:
                last_node.next = head.next
            else:
                last_node = head
            
            head = head.next
            
        return new_head