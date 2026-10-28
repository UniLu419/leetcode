from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left = [g - c for g, c in zip(gas, cost)]

        n = len(left)
        for i in range(n):
            temp = left[i]
            finished = True
            if temp < 0:
                continue
            for j in range(1, n):
                temp += left[(i + j) % n]
                if temp < 0:
                    finished = False
                    break
            if finished:
                return i
        return -1
