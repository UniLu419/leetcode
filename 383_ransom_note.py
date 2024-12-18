from typing import List
from timing_dec import timing


class Solution:
    @timing
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map_r = {}
        hash_map_m = {}
        for j in magazine:
            if j in hash_map_m:
                hash_map_m[j] += 1
            else:
                hash_map_m[j] = 1
        for i in ransomNote:
            if i not in hash_map_m:
                return False

            if i in hash_map_r:
                hash_map_r[i] += 1
            else:
                hash_map_r[i] = 1

            if hash_map_m[i] < hash_map_r[i]:
                return False
        return True

    # hash完后统一判断快一点
    @timing
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        hash_map_r = {}
        hash_map_m = {}
        for j in magazine:
            if j in hash_map_m:
                hash_map_m[j] += 1
            else:
                hash_map_m[j] = 1
        for i in ransomNote:
            if i in hash_map_r:
                hash_map_r[i] += 1
            else:
                hash_map_r[i] = 1

        for key in hash_map_r.keys():
            if key not in hash_map_m or hash_map_m[key] < hash_map_r[key]:
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
                    ransomNote = "a"
                    magazine = "b"
                case 2:
                    # sample 2
                    ransomNote = "aa"
                    magazine = "ab"
                case 3:
                    # sample 3
                    ransomNote = "aa"
                    magazine = "aab"
                case _:
                    break
            print(f"ans = {solution.canConstruct(ransomNote,magazine)}")
            print(f"ans = {solution.canConstruct2(ransomNote,magazine)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
