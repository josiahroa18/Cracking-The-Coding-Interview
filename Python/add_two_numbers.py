'''
LeetCode link: https://leetcode.com/problems/add-two-numbers/submissions/

###### Problem ######
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Understand: I am guaranteed to be given a linked list representing non-negative integers.
Each node contains a single digit
The digits for the integer are stored in a reverse order in the linked list:
- The head represents the ones place
I need to return the sum as a linked list in reverse order as well

Questions:
Can I assume that the length of l1 and l2 are the same?

Plan: 
1. Set a carry variable: boolean to keep track of carry status
2. Create the head of a new LL
3. Loop through l1 until l1.next is None
     1. Take the sum
     2. Check to see if carry is True: add 1 if so
     3. Check to see if the new sum is double digit: subtract 10 and set carry to True if so
     4. Assign new node and link it
     5. Increment nodes to next node
4. Check to see if there is one final carry: Create node with value of 1 if so
5. Return new LL

Execute:
'''
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         carry = False
#         head = None
#         curr = None
#         while l1 is not None:
#             _sum = l1.val + l2.val
#             if carry:
#                 _sum += 1
#                 carry = False
            
#             if _sum > 9:
#                 carry = True
#                 _sum -= 10
                
#             if head is None:
#                 head = ListNode(_sum)
#                 curr = head
#             else:
#                 curr.next = ListNode(_sum)
#                 curr = curr.next
            
#             l1 = l1.next
#             l2 = l2.next
        
#         if carry:
#             curr.next = ListNode(1)
            
#         return head
'''
Reflect:
Time Complexity is O(n)
Space Complexity is O(n)
This solution only works if the length of l1 and l2 are the same. But what if they aren't?

Plan:
1. Create a sum variable to hold the current sum
2. Create the head of the new LL
3. Loop through while l1, l2, or _sum are False/0: This handles left over carry at the end
    1. If l1 is not None: Add value of l1 to sum and move to next node
    2. If l2 is not None: Add value of l2 to sum and move to next node
    3. Set the current node's next to a new node with the sum % 10 to handle the carry
    4. Move to the next current node
    5. Get the carry value using integer divide and store it in sum
4. Return head.next since we initialized with a placeholder node

Execute:
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _sum = 0
        head = ListNode(0)
        curr = head
        while l1 or l2 or _sum:
            if l1:
                _sum += l1.val
                l1 = l1.next
            if l2:
                _sum += l2.val
                l2 = l2.next
            curr.next = ListNode(_sum % 10)
            curr = curr.next
            _sum //= 10
                
        return head.next 
'''
Reflect:
Time Complexity is O(n)
Space Complexity is O(n)
This solution actually works because it handles cases where l1 > l2 or l2 > l1
Carry system improved by using python math operators
'''
        