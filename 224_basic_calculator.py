from typing import List
from timing_dec import timing


class Solution:
    @timing
    def calculate(self, s: str) -> int:
        # 处理加减数学计算除了把数和运算符丢进栈以外还可以把括号前的运算符（1/-1）丢进栈
        s = s.replace(" ", "")
        sign_stack = [1]
        num = 0
        operation = 1
        ans = 0
        for char in s:
            if char.isnumeric():
                num = num * 10 + int(char)
                continue
            ans += operation * num
            num = 0
            match char:
                case "+":
                    operation = sign_stack[-1]
                case "-":
                    operation = -sign_stack[-1]
                case "(":
                    sign_stack.append(operation)
                case ")":
                    sign_stack.pop()
        ans += operation * num
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
                    s = "1 + 1"
                case 2:
                    # sample 2
                    s = " 2-1 + 2 "
                case 3:
                    # sample 3
                    s = "(1+(4+5+2)-3)+(6+8)"
                case 4:
                    # sample 4
                    s = "1-(     -2)"
                case _:
                    break
            print(f"ans = {solution.calculate(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
