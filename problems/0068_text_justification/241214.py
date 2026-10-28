from typing import List


class Solution:
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
