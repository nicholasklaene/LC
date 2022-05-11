"""
Hashmap - could also be solved in O(nlogn) with O(1) space if 
space is an issue by sorting & using two pointers. 

Time: O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i
        return [-1, -1]
