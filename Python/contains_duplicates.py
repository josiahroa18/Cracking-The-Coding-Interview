'''
LeetCode link: https://leetcode.com/problems/contains-duplicate/submissions/

###### Problem ######
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

'''
Understand: I need to check the array given to me for any duplicate.
If any number appears once, I should return True

Plan: 
Create a hashtable
Loop through the array for each index
- If value at index i is in hashtable: return True
- If value at index is in not in hastable: add it and continue

return False

Execute:
'''
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         values = {}
#         for i in range(len(nums)):
#             if nums[i] in values:
#                 return True
#             else:
#                 values[nums[i]] = True
#         return False
'''
Reflect: 
Runtime is O(n) - 77% of submissions
Space Complexity is O(n) - 22% of submissions
Can I use sets to make this quicker?
'''

'''
Plan:
Create a set of the nums given, this will automatically mask out any duplicates
Compare the length of the list of nums to the set:
- The length of the set will be smaller if there are duplicates
- The length of the set will be equal if there are no duplicates

Execute:
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
'''
Reflect:
Runtime is O(n) but runs slower than the previous solution - 18% of submissions
Space Complexity is O(n) but uses less space than the previous solution - 96% of submissions
'''
        


        
        
        