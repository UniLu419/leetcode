from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # 先证明一定有解
        if sum(gas) < sum(cost):
            return -1

        start = 0
        remain = 0
        # 使用贪心思想
        for n in range(len(gas)):
            # while n < len(gas):
            remain = remain + gas[n] - cost[n]
            if remain >= 0:
                continue
                # n += 1
            else:
                start = n + 1
                remain = 0
                # n += 1
        return start
