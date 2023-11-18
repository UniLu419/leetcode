from typing import List, Optional
from custom_types import TreeNode
from utils import list_to_tree, string_to_int_list


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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            tree_list = string_to_int_list(input("tree_list: "))
            root = list_to_tree(tree_list)
            print(f"ans = {solution.inorderTraversal(root)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
