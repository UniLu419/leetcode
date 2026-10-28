class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 首先返回不需处理的字符串
        if numRows < 2:
            return s

        # 使用ans记录每一行的字符串
        n = len(s)
        ans = [""] * numRows

        # 计算一个周期的步长
        step = 2 * numRows - 2

        for i in range(n):
            # mod步长的余数为单一周期内index（0-index）
            remainder = i % step

            # 周期内前半数照常放入ans，后半数为周期步长-余数
            if remainder + 1 <= numRows:
                ans[remainder] += s[i]
            else:
                ans[step - remainder] += s[i]
        # 拼接后返回
        return "".join(ans)
