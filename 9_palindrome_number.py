class Solution:
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


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        reversed = 0
        while temp > 0:
            tail = temp % 10
            reversed = reversed * 10 + tail
            temp = temp // 10
        return reversed == x


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("x =")
            print(f"ans = {solution.isPalindrome(int(s))}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
