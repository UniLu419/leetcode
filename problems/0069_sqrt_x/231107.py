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
