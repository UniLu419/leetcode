from typing import List, Optional
from custom_types import TreeNode
from utils import print_tree_inorder_traversal, string_to_int_list


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sorted_array_to_BST(nums, 0, len(nums) - 1)

    def sorted_array_to_BST(
        self, nums: List[int], start: int, end: int
    ) -> Optional[TreeNode]:
        length = end - start + 1
        if length == 2:
            current = TreeNode(nums[end])
            current.left = TreeNode(nums[start])
            return current
        if length == 1:
            return TreeNode(nums[start])
        mid = length // 2 + start
        current = TreeNode(nums[mid])
        current.left = self.sorted_array_to_BST(nums, start, mid - 1)
        current.right = self.sorted_array_to_BST(nums, mid + 1, end)
        return current


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            tree_list = string_to_int_list(input("tree_list: "))
            root = solution.sortedArrayToBST(tree_list)
            print_tree_inorder_traversal(root)
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
