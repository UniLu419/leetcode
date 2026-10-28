from typing import Optional
from helpers import TreeNode


class Solution:
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
