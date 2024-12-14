from typing import List
from timing_dec import timing


class Solution:
    @timing
    def reverseWords(self, s: str) -> str:
        words = s.split()
        l, r = 0, len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return " ".join(words)


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    s = "the sky is blue"
                case 2:
                    # sample 2
                    s = "  hello world  "
                case 3:
                    # sample 3
                    s = "a good   example"
                case _:
                    break
            print(f"ans = {solution.reverseWords(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()


# 如果是要空间复杂度O（1）的话，可以将字符串去掉冗余空格后整体反转，然后再将每个单词反转
