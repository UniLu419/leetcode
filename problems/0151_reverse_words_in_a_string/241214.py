class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        l, r = 0, len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return " ".join(words)


# 如果是要空间复杂度O（1）的话，可以将字符串去掉冗余空格后整体反转，然后再将每个单词反转
