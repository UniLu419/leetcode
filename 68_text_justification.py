from typing import List
from timing_dec import timing


class Solution:
    @timing
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n = len(words)
        current = []
        current_word_len = 0
        for i in range(n):
            word_length = len(words[i])

            # handle words[i] in this line
            if current_word_len + len(current) + word_length <= maxWidth:
                current.append(words[i])
                current_word_len += word_length
                continue
            # handle words[i] in next line
            # finish current line
            if len(current) == 1:  # lines only have one word
                line = current[0] + " " * (maxWidth - current_word_len)
                ans.append(line)
                current.clear()
                current.append(words[i])
                current_word_len = word_length
                continue
            # regular lines
            total_space = maxWidth - current_word_len
            space_cnt = len(current) - 1
            quotient, remainder = divmod(total_space, space_cnt)
            line = current[0]
            for j in range(1, space_cnt + 1):
                line += " " * quotient
                if remainder >= j:
                    line += " "
                line += current[j]
            ans.append(line)
            current.clear()
            current.append(words[i])
            current_word_len = word_length
        # finish last line
        temp = " ".join(current)
        line = temp + " " * (maxWidth - len(temp))
        ans.append(line)

        return ans

    @timing
    def fullJustify2(self, words: List[str], maxWidth: int) -> List[str]:
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    words = [
                        "This",
                        "is",
                        "an",
                        "example",
                        "of",
                        "text",
                        "justification.",
                    ]
                    maxWidth = 16
                case 2:
                    # sample 2
                    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
                    maxWidth = 16
                case 3:
                    # sample 3
                    words = [
                        "Science",
                        "is",
                        "what",
                        "we",
                        "understand",
                        "well",
                        "enough",
                        "to",
                        "explain",
                        "to",
                        "a",
                        "computer.",
                        "Art",
                        "is",
                        "everything",
                        "else",
                        "we",
                        "do",
                    ]
                    maxWidth = 20
                case _:
                    break
            print(f"ans = {solution.fullJustify(words,maxWidth)}")
            print(f"ans = {solution.fullJustify2(words,maxWidth)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
