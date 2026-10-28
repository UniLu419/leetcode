class Solution:
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
