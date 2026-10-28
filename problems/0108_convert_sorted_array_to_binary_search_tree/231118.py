from typing import List, Optional
from helpers import TreeNode


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
