from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []  # 当前行单词
        article = []  # 结果
        str_len = 0  # 当前行纯字符长度
        for w in words:
            # 如果新单词长度+当前空格个数+当前行纯字符长度 >= 最大宽度 则无法添加新单词
            # 这里由于空行一定会可以添加，所以直接用len(line) - 1表示当前空格个数不影响结果
            # 如果当前单词插不进去当前行，意味着当前行已结束，可以开始处理
            if len(w) + len(line) - 1 + str_len >= maxWidth:
                # 处理第i个待插入空格
                for i in range(maxWidth - str_len):
                    # 第i（0-indexed）个空格的插入位置是 i除以可插入空格的位置的余数
                    line[i % max(len(line) - 1, 1)] += " "
                # 将处理完的行插入结果
                article.append("".join(line))
                # 初始化行
                line = []
                str_len = 0
            # 当前单词可以插入当前行
            line.append(w)
            str_len = str_len + len(w)
        # 处理最后一行 可以使用str.ljust(目标长度)来在字符串右端插入空格补齐长度
        article = article + [" ".join(line).ljust(maxWidth)]
        return article
