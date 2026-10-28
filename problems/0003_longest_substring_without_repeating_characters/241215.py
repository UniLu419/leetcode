class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map: dict[str, int] = {}
        max_len = 0
        n = len(s)
        l, r = 0, -1
        while l < n and r < n:
            length = r - l + 1
            if length > max_len:
                max_len = length

            r += 1
            if r < n:
                # 和之前239求固定长度子序列最大值那道题一样，需要注意下标是否在窗口内
                if s[r] in hash_map and hash_map[s[r]] >= l:
                    l = hash_map[s[r]] + 1
                    hash_map[s[r]] = r
                else:
                    hash_map[s[r]] = r
        return max_len
