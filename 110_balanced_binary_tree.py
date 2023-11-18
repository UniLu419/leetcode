from typing import List, Optional
from custom_types import TreeNode
from utils import list_to_tree, string_to_int_list


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left = self.get_tree_layer_number(root.left)
        right = self.get_tree_layer_number(root.right)
        result = left - right if left > right else right - left
        if result > 1:
            return False
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        return True

    def get_tree_layer_number(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.get_tree_layer_number(root.left)
        right = self.get_tree_layer_number(root.right)
        if left > right:
            return left + 1
        return right + 1


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            tree_list = string_to_int_list(input("tree_list: "))
            root = list_to_tree(tree_list)
            print(f"ans = {solution.isBalanced(root)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
