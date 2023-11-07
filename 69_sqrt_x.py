class Solution:
    def mySqrt(self, x: int) -> int:
        guess = 0.5 * x
        while True:
            if guess**2 <= x and (guess // 1 + 1) ** 2 > x:
                return int(guess // 1)
            next = 0.5 * (guess + x / guess)
            if guess // 1 == next // 1:
                return int(guess // 1)
            guess = next


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("x = ")
            print(f"ans = {solution.mySqrt(int(s))}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
