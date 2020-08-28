'''
LeetCode Link: https://leetcode.com/problems/find-the-duplicate-number/

###### Problem ######
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

'''
Understand: 
I'm given an array of nums and need to find which number is a duplicate in the given array
I can assume that there is only one duplicate number
I cannot modify the array
Space must be consant O(1)
Runtime must be less than O(n^2)

Plan:
My first thought was to use either hashtables, sorting and adjacent duplicates, or a set but due to the contstraint that has been given, we need to use a different algorithm.

This algorithm is called the Tortoise and Hare (Cycle Detection)
By accessing the num at each index and using it as the next index, we can find a cycle in the array.
Once we find the cycle, we need to find the entrance.
To find the entrance, we create two pointers.
A fast pointer - Moves two indices at a time
A slow pointer - Moves one index at a time
Keep moving the pointers until they meet. This will be the intersection point.
Reset the slow pointer to the first index.
Now move both pointers one at a time until they meet again.
When they meet again, this will find the entrance to the cycle and the value at that index will be a duplicate in the array.


Execute:
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return fast
    
'''
Reflect:
Time Complexity: O(n)
Space Complexity: O(1)
'''