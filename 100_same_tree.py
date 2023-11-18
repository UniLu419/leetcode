from typing import List, Optional
from custom_types import TreeNode
from utils import list_to_tree, string_to_int_list


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            p_tree_list = string_to_int_list(input("p_tree_list: "))
            q_tree_list = string_to_int_list(input("q_tree_list: "))
            p_root = list_to_tree(p_tree_list)
            q_root = list_to_tree(q_tree_list)
            print(f"ans = {solution.isSameTree(p_root,q_root)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
