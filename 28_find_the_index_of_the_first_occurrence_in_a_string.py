class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            same = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    same = False
                    break
            if same:
                return i
        return -1


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            haystack = input("Please enter the original string: ")
            needle = input("Please enter the string to search: ")
            print(f"k = {solution.strStr(haystack,needle)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
