class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a = [0] * n
        a[0] = 1
        a[1] = 2
        for i in range(2, n):
            a[i] = a[i - 1] + a[i - 2]
        return a[n - 1]


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("Please enter a list of int separated with single space: ")
            print(f"ans = {solution.solve(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
