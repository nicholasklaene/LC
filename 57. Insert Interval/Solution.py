"""
Two fundamental problems:
- How do we know when two intervals overlap?
- How do we merge those intervals

Once this is figured out, simply loop through the intervals,
merge them if our new interval and intervals[i] overlap
and insert accordingly

Tempting to do a binary search since they are sorted,
but worse case is that EVERY interval will need to be merged
so this is O(N)

Time: O(N)
Space: O(N) if you count the output list, O(1) otherwise
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(interval1: List[int], interval2: List[int]) -> bool:
            if interval1[0] > interval2[0]:
                interval1, interval2 = interval2, interval1
            return interval2[0] >= interval1[0] and interval2[0] <= interval1[1]

        def merge(interval1: List[int], interval2: List[int]) -> bool:
            start, end = min(interval1[0], interval2[0]), max(
                interval1[1], interval2[1])
            return [start, end]

        answer = []
        i, inserted = 0, False
        while i < len(intervals):
            if overlap(intervals[i], newInterval):
                newInterval = merge(intervals[i], newInterval)
                i += 1
            elif not inserted and newInterval[0] < intervals[i][0]:
                answer.append(newInterval)
                inserted = True
            else:
                answer.append(intervals[i])
                i += 1

        if not inserted:
            answer.append(newInterval)
        return answer
