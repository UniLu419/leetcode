from typing import List


class Solution:
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
