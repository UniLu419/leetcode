from typing import List
from timing_dec import timing


class Solution:
    @timing
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        parsed_s = [char for char in s if char.isalnum()]
        l, r = 0, len(parsed_s) - 1
        while l < r:
            if parsed_s[l] != parsed_s[r]:
                return False
            l += 1
            r -= 1
        return True

    @timing
    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        parsed_s = [char for char in s if char.isalnum()]
        return parsed_s == parsed_s[::-1]


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    s = "A man, a plan, a canal: Panama"
                case 2:
                    # sample 2
                    s = "race a car"
                case 3:
                    # sample 3
                    s = " "
                case _:
                    break
            print(f"ans = {solution.isPalindrome(s)}")
            print(f"ans = {solution.isPalindrome2(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
