from typing import List
from timing_dec import timing


class Solution:
    @timing
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split()[-1]
        return len(ans)

    @timing
    def lengthOfLastWord2(self, s: str) -> int:
        n = len(s)
        ans = 0
        start = False
        for i in range(n):
            if s[n - 1 - i] != " ":
                start = True
                ans += 1
            elif start:
                break
        return ans


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    s = "Hello World"
                case 2:
                    # sample 2
                    s = "   fly me   to   the moon  "
                case 3:
                    # sample 3
                    s = "luffy is still joyboy"
                case _:
                    break
            print(f"ans = {solution.lengthOfLastWord(s)}")
            print(f"ans = {solution.lengthOfLastWord2(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
