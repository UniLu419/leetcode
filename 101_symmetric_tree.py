from typing import Optional
from custom_types import TreeNode
from utils import list_to_tree, string_to_int_list


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_tree_queue = [root.left]
        right_tree_queue = [root.right]
        while len(left_tree_queue) != 0 and len(right_tree_queue) != 0:
            left_current = left_tree_queue.pop(0)
            right_current = right_tree_queue.pop(0)
            if left_current is None and right_current is None:
                continue
            if left_current is None or right_current is None:
                return False
            if left_current.val != right_current.val:
                return False
            left_tree_queue.append(left_current.left)
            left_tree_queue.append(left_current.right)
            right_tree_queue.append(right_current.right)
            right_tree_queue.append(right_current.left)
        return True


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            tree_list = string_to_int_list(input("tree_list: "))
            root = list_to_tree(tree_list)
            print(f"ans = {solution.isSymmetric(root)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
