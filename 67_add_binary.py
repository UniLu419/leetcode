class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans_len = max(len(a), len(b)) + 1
        ans_array = ["0"] * ans_len
        inc = 0
        formatted_a = "0" * (ans_len - len(a)) + a
        formatted_b = "0" * (ans_len - len(b)) + b
        for i in range(ans_len):
            index = ans_len - 1 - i
            ans, new_inc = self.add(int(formatted_a[index]), int(formatted_b[index]))
            ans, inc = self.add(ans, inc)
            inc = new_inc or inc
            ans_array[index] = str(ans)

        return "".join(ans_array if ans_array[0] == "1" else ans_array[1:])

    def add(self, a: bool, b: bool):
        ans = a ^ b
        inc = a and b
        return ans, inc


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            a = input("Please enter string a: ")
            b = input("Please enter string b: ")
            print(f"ans = {solution.addBinary(a,b)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
