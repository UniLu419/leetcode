from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary: dict[int, int] = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        max = None
        for key in dictionary.keys():
            if max is None:
                max = key
            if dictionary[key] > dictionary[max]:
                max = key
        return max
