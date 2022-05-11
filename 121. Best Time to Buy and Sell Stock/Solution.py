"""
Two Pointer Technique

Keep a left and right pointer
if at any point prices[left] < prices[right], then there is no point in buying here.
That would be a loss. Move left over to right and increment right.
Then, calculate the profit, check if it is the biggest we've seen and increment right.

Time: O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        l, r = 0, 0
        while r < len(prices):
            if prices[l] > prices[r] and l < r:
                l, r = r, r + 1
                continue
            profit = prices[r] - prices[l]
            answer = max(answer, profit)
            r += 1
        return answer
