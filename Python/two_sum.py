'''
LeetCode Link: https://leetcode.com/problems/two-sum/

###### Problem ######

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


'''
Understand: Return the indices of two numbers that add up to
a specific target
There is exactly one solution
Indices cannot be the same

Plan:
1. Create a hashtable for found nums in the nums list
2. Loop through the list of nums
3. For each num, calculate the difference
      difference = target - current_num
4. If the difference has been found, return [current_index, index of difference]
   Otherwise, store the current_num in the hashtable
   
Execute:
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in cache:
                return [i, cache[difference]]
            else:
                cache[nums[i]] = i
                
'''
Reflect:
Time Complexity is O(n)
Space Complexity is O(n)

Plan:
1. Sort the incoming list of nums
2. Create a left pointer for the start of the list and a right pointer for the end
3. Loop through the nums and get the sum of left pointer and right pointer
   - If sum is greater: move right pointer down
   - If sum is less: move left pointer up
   - If sum is equal to target: return [left_pointer, right_pointer]
   
Execute:
'''
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         left = 0
#         right = len(nums) - 1
#         while True:
#             _sum = nums[left] + nums[right]
#             if _sum > target:
#                 right -= 1
#             elif _sum < target:
#                 left += 1
#             else:
#                 return [left, right]
'''
Reflect:
This solution won't work for this problem since we are returning the index. When we sort, we lost the
original index and therefore won't get the expect result.
Time Complexity: O(nlogn)
Space Complexity: O(1)
'''

                
        
        