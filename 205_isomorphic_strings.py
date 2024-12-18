from typing import List
from timing_dec import timing


class Solution:
    @timing
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if len(t) != n:
            return False
        hash_map1 = {}
        hash_map2 = {}  # 注意这里要求不同字母不可以映射到同一个字母上，所以需要双向hash
        for i, j in zip(s, t):
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
                    s = "egg"
                    t = "add"
                case 2:
                    # sample 2
                    s = "foo"
                    t = "bar"
                case 3:
                    # sample 3
                    s = "paper"
                    t = "title"
                case 4:
                    # sample 4
                    s = "badc"
                    t = "baba"
                case _:
                    break
            print(f"ans = {solution.isIsomorphic(s,t)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
