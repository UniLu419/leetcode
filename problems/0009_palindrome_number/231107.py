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
