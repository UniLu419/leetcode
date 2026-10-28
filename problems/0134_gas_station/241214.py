from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left = []
        sum_left = 0
        for g, c in zip(gas, cost):
            t = g - c
            left.append(t)
            sum_left += t
        if sum_left < 0:
            return -1
        n = len(left)
        for i in range(n):
            temp = 0
            finished = True
            for j in range(n):
                temp += left[(i + j) % n]
                if temp < 0:
                    finished = False
                    break
            if finished:
                return i
        return -1
