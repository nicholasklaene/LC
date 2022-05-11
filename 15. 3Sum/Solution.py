"""
Sort & use two pointers to solve two sum for each number

The tricky part is removing duplicates. For the outer for loop, just check
if nums[i] == nums[i - 1]. The two pointer loop is trickier, use an oldL and oldR
variable to simplify it

Time: O(n^2)
Space: O(n) - sorting
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    answer.append([num, nums[l], nums[r]])
                    oldL, oldR = nums[l], nums[r]
                    while l < len(nums) and nums[l] == oldL:
                        l += 1
                    while r > 0 and nums[r] == oldR:
                        r -= 1
        return answer
