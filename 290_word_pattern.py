from typing import List
from timing_dec import timing


class Solution:
    @timing
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map1 = {}
        hash_map2 = {}
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        for i, j in zip(s_list, pattern):
            if i not in hash_map1:
                if j in hash_map2:
                    return False
                hash_map1[i] = j
                hash_map2[j] = i
            elif hash_map1[i] != j:
                return False
        return True


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    pattern = "abba"
                    s = "dog cat cat dog"
                case 2:
                    # sample 2
                    pattern = "abba"
                    s = "dog cat cat fish"
                case 3:
                    # sample 3
                    pattern = "aaaa"
                    s = "dog cat cat dog"
                case _:
                    break
            print(f"ans = {solution.wordPattern(pattern,s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
