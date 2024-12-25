from typing import List, Optional
from timing_dec import timing


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next: Optional[Node] = next
        self.random: Optional[Node] = random


class Solution:
    @timing
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        hash_map = {}
        if not head:
            return None
        old = head
        ans: Optional[Node] = None
        current: Optional[Node] = None
        while old:
            if not current:
                ans = Node(old.val)
                current = ans
            else:
                temp = Node(old.val)
                current.next = temp
                current = temp
            hash_map[id(old)] = current
            old = old.next

        old = head
        current = ans
        while old:
            if old.random:
                current.random = hash_map[id(old.random)]
            else:
                current.random = None
            current = current.next
            old = old.next
        return ans


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    k = 3
                case 2:
                    # sample 2
                    k = 2
                case 3:
                    # sample 3
                    k = 3
                case _:
                    break
            print(f"ans = {solution.solve(k)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
