'''
Given a package with a weight limit limit and an array of integers items of where each integer represents the weight of an item, implement a function merge_packages that finds the first two items in the items array whose sum of weights equals the given weight limit limit.

Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

Examples:
Input: items = [4, 6, 10, 15, 16], limit = 21
Output: [3, 1]
Explanation: The weight of the items at indices 3 and 1 sum up to the specified limit.

Understand:
I need to find two items in the items array that equal up to the limit
This is just another version of the twoSum problem
Return the array where [i, j] and i > j
If no pair exists, return an empty array

Plan:
Loop through the items and store every value in a hashtable
As we loop through the array, use difference = limit - current_value to get the difference
We can then check the hashtable to see if that difference exists in the given a array
- If it does, return the pair
At the end of the loop, if no pair has been found, return an empty array
'''
def merge_packages(items, limit):
    found = {}
    for i in range(len(items)):
        difference = limit - items[i]
        if difference in found:
            if i > found[difference]:
                return [i, found[difference]]
            else:
                return [found[difference], i]
        else:
            found[items[i]] = i
    return []

'''
Reflect:
Time complexity is O(n) since we loop through the items array once
Space complexity is O(n) since we use a hashtable to store item and index
'''