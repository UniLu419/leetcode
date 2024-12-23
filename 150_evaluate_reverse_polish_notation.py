from ast import Num
from typing import List
from timing_dec import timing


class Solution:
    @timing
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            match token:
                case "+":
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(a + b)
                case "-":
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(a - b)

                case "*":
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(a * b)

                case "/":
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(int(a / b))

                case _:
                    num_stack.append(int(token))
        return num_stack.pop()


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    tokens = ["2", "1", "+", "3", "*"]
                case 2:
                    # sample 2
                    tokens = ["4", "13", "5", "/", "+"]
                case 3:
                    # sample 3
                    tokens = [
                        "10",
                        "6",
                        "9",
                        "3",
                        "+",
                        "-11",
                        "*",
                        "/",
                        "*",
                        "17",
                        "+",
                        "5",
                        "+",
                    ]
                case _:
                    break
            print(f"ans = {solution.evalRPN(tokens)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
