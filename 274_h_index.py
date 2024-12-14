from typing import List
from timing_dec import timing


class Solution:
    @timing
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
        return h


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    citations = [3, 0, 6, 1, 5]
                case 2:
                    # sample 2
                    citations = [1, 3, 1]
                case _:
                    break
            print(f"ans = {solution.hIndex(citations)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
