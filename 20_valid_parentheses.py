from typing import List
from timing_dec import timing


class Solution:
    @timing
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            match char:
                case "(":
                    stack.append("(")
                case "[":
                    stack.append("[")
                case "{":
                    stack.append("{")
                case ")":
                    if not stack:
                        return False
                    t = stack.pop()
                    if t != "(":
                        return False
                case "]":
                    if not stack:
                        return False
                    t = stack.pop()
                    if t != "[":
                        return False
                case "}":
                    if not stack:
                        return False
                    t = stack.pop()
                    if t != "{":
                        return False
        return not stack


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    s = "()"
                case 2:
                    # sample 2
                    s = "()[]{}"
                case 3:
                    # sample 3
                    s = "(]"
                case 4:
                    # sample 4
                    s = "([])"
                case _:
                    break
            print(f"ans = {solution.isValid(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
