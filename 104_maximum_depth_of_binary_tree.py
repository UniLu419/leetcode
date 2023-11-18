from typing import Optional
from custom_types import TreeNode
from utils import list_to_tree, string_to_int_list


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if left_depth < right_depth:
            return right_depth + 1
        else:
            return left_depth + 1


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        current_queue = [root]
        depth = 0
        next_queue = []
        while len(current_queue) != 0:
            depth += 1
            while len(current_queue) != 0:
                current = current_queue.pop(0)
                if current.left is not None:
                    next_queue.append(current.left)
                if current.right is not None:
                    next_queue.append(current.right)
            if len(next_queue) != 0:
                current_queue = next_queue
                next_queue = []
        return depth


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            tree_list = string_to_int_list(input("tree_list: "))
            root = list_to_tree(tree_list)
            print(f"ans = {solution.maxDepth(root)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
