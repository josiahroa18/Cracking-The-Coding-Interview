'''
Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

For example, if we have the following linked list: 
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).

After the function executes, the state of the linked list should be:
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

If k is longer than the length of the linked list, the linked list should not be changed.

Can you implement a solution that performs a single pass through the linked list and doesn't use any extra space?

Note: When reading the tests, the linked list contents are enumerated in between square brackets; this does NOT mean the inputs are arrays.

For example, a test input of head: [2, 4 ,6] indicates that the input is a singly-linked list
(2) -> (4) -> (6) -> null whose head is the first element in the linked list.
'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
'''
Understand:
Removing kth node from the end of the Linked List
I'm given the head node and the k value
I need to return the head of the updated Linked List

Plan:
Have a current pointer that traverses the Linked List (curr)
Have a trailing pointer kth nodes behind the current pointer (trail)
Have another trailing pointer one node behind the original trailing pointer (prev)

Once we reach the end, reference the trailing pointer and second trailing pointer to remove the node

Edge Cases:
k is equal to 0
k is longer than the length of the Linked List
node to be removed is the head node
node to be removed is the tail node
'''
def remove_kth_from_end(head, k):
    if k == 0:
        return head
    counter = 0 # Represents the number of nodes we have traversed
    curr = head
    trail = None
    prev = None
    # Loop until curr.next is None
    while curr.next:
        # Figure out when to assign the trail and prev pointer
        if counter == k - 1:
            print('Assigning trail')
            trail = head
        if counter == k:
            prev = head
        
        # Update the pointers as we traverse
        curr = curr.next
        if trail:
            trail = trail.next
        if prev:
            prev = prev.next
        counter += 1
    
    # PAUSE: test that all pointers are poiting to the appropiate nodes
    # print(f"Current: {curr.value}") # Should be 11
    # print(f"Trail: {trail.value}") # Should be 14
    # print(f"Prev: {prev.value}") # Should be 15
    
    # All pointers should be poiting to the appropiate nodes
    
    # Make sure that k is not longer than the length(counter + 1) of the Linked List
    if k > counter + 1: 
        return head
        
    # Check to see if the head node is the node to be removed
    # counter == 1 implies that the trail pointer would be pointing at the head node
    if counter == 1:
        head = head.next
        return head
        
    # Delete the node from the LinkedList
    prev.next = trail.next
    return head
    
'''
Reflect:
Time complexity is O(n) since we are looping through the linked list one time
Space complexity is O(1) since we are not allocating space for any other data structure
  and doing in place removal
'''
    
    
        

