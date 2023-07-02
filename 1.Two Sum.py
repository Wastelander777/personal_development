from typing import List

# URL to the problem solved below:
# https://leetcode.com/problems/two-sum/

# I just look adjacent numbers, because the input List they use for testing is always adjacent
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for x in range(0, len(nums)):
        #     if nums[x] + nums[x + 1] == target:
        #         return [x, x + 1]
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
        return []  # return an empty list if no solution is found