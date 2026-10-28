from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        merged_left = [0]
        start = [0]  # the original index of merged_left
        sum = 0
        for i in range(n):
            t = gas[i] - cost[i]
            sum += t
            if merged_left[-1] * t >= 0:
                merged_left[-1] += t
            else:
                start.append(i)
                merged_left.append(t)
        if sum < 0:
            return -1
        m = len(merged_left)
        for i in range(m):
            temp = 0
            finished = True
            for j in range(m):
                temp += merged_left[(i + j) % m]
                if temp < 0:
                    finished = False
                    break
            if finished:
                return start[i]
        return -1
