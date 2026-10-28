from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table: 
                hash_table[nums[i]].append(i)
            else:
                hash_table[nums[i]] = [i]
            ans = target - nums[i]
            if ans in hash_table:
                if ans == nums[i]:
                    if len(hash_table[ans]) > 1:
                        return [hash_table[ans][0], hash_table[ans][1]]
                    else:
                        continue
                else:
                    return [hash_table[ans][0], i]
        return []
             
