"""
Backtracking permutations solution
Calculate permutations of the 4 characters 
and select the largest valid time

Time: permutations are O(N!), but N is always 4, so this is O(1)
Space: O(N), but N is always 4, so O(1)
"""


from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def timeVal(time: List[int]):
            hours = int(f"{time[0]}{time[1]}")
            minutes = int(f"{time[2]}{time[3]}")
            return hours * 60 + minutes

        def valid(current: List[int]) -> bool:
            return (
                int(f"{current[0]}{current[1]}") < 24
                and
                int(f"{current[2]}{current[3]}") < 60
            )

        def toTimeString(time: List[int]):
            if Global.answer[0] == -1:
                return ""
            return f"{Global.answer[0]}{Global.answer[1]}:{Global.answer[2]}{Global.answer[3]}"

        class Global:
            answer = [-1, -1, -1, -1]

        def permute(current: List[int], i: int, choices: List[int]):
            if i == 4 and (
                Global.answer[0] == -
                    1 or timeVal(current) > timeVal(Global.answer)
            ):
                Global.answer = current
                return

            numChoices = len(choices)
            for _ in range(numChoices):
                choice = choices.pop(0)
                current[i] = choice
                if valid(current):
                    permute(current[:], i + 1, choices[:])
                choices.append(choice)

        permute([0, 0, 0, 0], 0, arr)
        return toTimeString(Global.answer)
