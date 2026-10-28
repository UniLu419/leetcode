class Solution:
    # 由于这道题提到了结果是1或者loop，则一定会有元素被重复计算，所以可以用hash map来存放计算结果，如果有计算过的证明进入loop
    def isHappy(self, n: int) -> bool:
        hash_map = {}
        if n == 1:  # 注意边界条件
            return True
        current = n
        while current != 1:
            temp = self.calculate(current)
            if temp == 1:
                return True
            if current not in hash_map:
                hash_map[current] = temp
                current = temp
            else:
                return False

    def calculate(self, n: int) -> int:
        n_list = [int(s) for s in str(n)]
        ans = 0
        for i in n_list:
            ans = ans + i * i
        return ans
