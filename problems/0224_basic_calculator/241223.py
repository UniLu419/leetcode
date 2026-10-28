class Solution:
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
