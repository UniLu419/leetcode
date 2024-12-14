from typing import List
from timing_dec import timing


class Solution:
    @timing
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

    @timing
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        left = [g - c for g, c in zip(gas, cost)]

        if sum(left) < 0:
            return -1
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

    @timing
    def canCompleteCircuit3(self, gas: List[int], cost: List[int]) -> int:
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

    @timing
    def canCompleteCircuit4(self, gas: List[int], cost: List[int]) -> int:
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

    @timing
    def canCompleteCircuit_(self, gas: List[int], cost: List[int]) -> int:

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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    gas = [1, 2, 3, 4, 5]
                    cost = [3, 4, 5, 1, 2]
                case 2:
                    # sample 2
                    gas = [2, 3, 4]
                    cost = [3, 4, 3]
                case 3:
                    # sample 3
                    gas = [5, 1, 2, 3, 4]
                    cost = [4, 4, 1, 5, 1]
                case 4:
                    # sample 4
                    gas = [5, 1]
                    cost = [1, 5]
                case _:
                    break
            print(f"ans = {solution.canCompleteCircuit(gas,cost)}")
            print(f"ans = {solution.canCompleteCircuit2(gas,cost)}")
            print(f"ans = {solution.canCompleteCircuit3(gas,cost)}")
            print(f"ans = {solution.canCompleteCircuit4(gas,cost)}")
            print(f"ans = {solution.canCompleteCircuit_(gas,cost)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
