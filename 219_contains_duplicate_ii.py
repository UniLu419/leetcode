from typing import List
from timing_dec import timing


class Solution:
    @timing
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                hash_map[num].append(i)
            else:
                hash_map[num] = [i]
        for value in hash_map.values():
            n = len(value)
            if n > 1:
                for j in range(n - 1):
                    if value[j + 1] - value[j] <= k:
                        return True
        return False

    @timing
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                if i - hash_map[num][len(hash_map[num]) - 1] <= k:
                    return True
                hash_map[num].append(i)
            else:
                hash_map[num] = [i]

        return False

    @timing
    def containsNearbyDuplicate3(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                if i - hash_map[num] <= k:
                    return True
                hash_map[num] = i
            else:
                hash_map[num] = i

        return False


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    nums = [1, 2, 3, 1]
                    k = 3
                case 2:
                    # sample 2
                    nums = [1, 0, 1, 1]
                    k = 1
                case 3:
                    # sample 3
                    nums = [1, 2, 3, 1, 2, 3]
                    k = 2
                case _:
                    break
            print(f"ans = {solution.containsNearbyDuplicate(nums,k)}")
            print(f"ans = {solution.containsNearbyDuplicate2(nums,k)}")
            print(f"ans = {solution.containsNearbyDuplicate3(nums,k)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
