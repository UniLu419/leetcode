from inspect import stack
from typing import List
from timing_dec import timing


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def main():
    # Your main code goes here
    solution = MinStack()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    k = [
                        "MinStack",
                        "push",
                        "push",
                        "push",
                        "getMin",
                        "pop",
                        "top",
                        "getMin",
                    ]
                    v = [[], [-2], [0], [-3], [], [], [], []]
                case _:
                    break
            obj: MinStack
            for key, value in zip(k, v):
                match key:
                    case "MinStack":
                        obj = MinStack()
                    case "push":
                        obj.push(value[0])
                        print(obj.stack)
                    case "pop":
                        obj.pop()
                        print(obj.stack)
                    case "top":
                        print(obj.top())
                    case "getMin":
                        print(obj.getMin())

        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
