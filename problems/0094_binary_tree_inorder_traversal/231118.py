from typing import List, Optional
from helpers import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans_list = []
        self.inorder(root, ans_list)
        return ans_list

    def inorder(self, root: Optional[TreeNode], pre_list: List[int]):
        if root is not None:
            self.inorder(root.left, pre_list)
            pre_list.append(root.val)
            self.inorder(root.right, pre_list)
