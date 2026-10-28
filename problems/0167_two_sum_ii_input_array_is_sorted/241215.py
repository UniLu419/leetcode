from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(numbers):
            if num in hash_map:
                hash_map[num].append(i + 1)
            else:
                hash_map[num] = [i + 1]
        for num in numbers:
            aim = target - num
            if aim in hash_map:
                ans = [hash_map[num][0]]
                for index in hash_map[aim]:
                    if index != ans[0]:
                        ans.append(index)
                        break
                return ans
