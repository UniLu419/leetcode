class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and romanDict[s[i]] < romanDict[s[i + 1]]:
                result -= romanDict[s[i]]
            else:
                result += romanDict[s[i]]
        return result


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        return self.checkString(str(x))

    def checkString(self, number_string: str) -> bool:
        head = number_string[0]
        tail = number_string[len(number_string) - 1]
        if head != tail:
            return False

        if len(number_string) > 2:
            return self.checkString(number_string[1:][:-1])

        return True


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("Please enter a roman string: ")
            print(f"ans = {solution.romanToInt(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
