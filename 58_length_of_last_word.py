class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " " + s
        i = len(s) - 1
        end: int = None
        while i >= 0:
            if s[i] != " ":
                if end is None:
                    end = i
                i -= 1
            else:
                if end is not None:
                    return end - i
                else:
                    i -= 1


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("Please enter a string: ")
            print(f"ans = {solution.lengthOfLastWord(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
