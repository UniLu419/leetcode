from typing import List, Optional
from timing_dec import timing


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    @timing
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            balance = self.isBalanced(root.left) and self.isBalanced(root.right)
            difference = self.maxDepth(root.left) - self.maxDepth(root.right)
            if difference > 1 or difference < -1:
                return False
            else:
                return True and balance

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalance2(self, root: Optional[TreeNode]) -> bool:
        # 使用-1记录false，非负数记录高度
        def high(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            l = high(root.left)
            if l == -1:
                return -1
            r = high(root.right)
            if r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1

        return high(root) != -1


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    k = 3
                case 2:
                    # sample 2
                    k = 2
                case 3:
                    # sample 3
                    k = 3
                case _:
                    break
            print(f"ans = {solution.solve(k)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
