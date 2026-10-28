from typing import Optional
from helpers import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
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
