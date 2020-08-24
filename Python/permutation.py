# https://leetcode.com/problems/permutations/

# Permutations
# Given a collection of distinct integers, return all possible permutations.
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Permutate:
    def __init__(self):
        self.result = []

    def permutate(self, nums):
        self.generate(nums, [])
        return self.result

    def generate(self, nums, current_permutation):
        if len(nums) == 0:
            self.result.append(current_permutation)
        for i in range(len(nums)):
            self.generate(nums[:i] + nums[i+1:], current_permutation+[nums[i]])


permutation = Permutate()
print(permutation.permutate([1, 2, 3]))

