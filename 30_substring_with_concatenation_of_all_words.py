from typing import List
from timing_dec import timing


class Solution:
    @timing
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target, n, step_length = 0, len(s), len(words[0])
        hash_map = {}  # 存该单词的下标
        target_count = {}  # 统计该单词在原数组中出现了几次
        for word in words:
            target += len(word)
            if word in target_count:
                target_count[word] += 1
            else:
                target_count[word] = 1
        ans = []
        # 因为单词以外的字符不一定是跟单词一样长度，所以需要对总字符串进行分割，
        # 即从（0，step_lenth-1）不同位置开始按照固定step_lenth长度进行分割
        for i in range(step_length):
            # 内部是纯滑动窗口
            l = i
            r = l - 1
            while l < n and r < n:
                length = r - l + 1
                print(
                    f"length: {length}, l: {l}, r: {r} target: {target} current: {s[l:r+1]}"
                )
                # 当滑动窗口和我们所求的words总长度相等时代表找到了答案，需要将第一个单词弹出
                if length == target:
                    ans.append(l)
                    l += step_length

                # 如果窗口长度不满，则需要看后续单词
                elif length < target:
                    next_r = r + step_length
                    # 若后续单词存在则继续处理，否则结束循环
                    if next_r < n:
                        temp = s[r + 1 : next_r + 1]
                        print(f"temp:{temp}")
                        # 若单词为目标单词，存入hash_map[当前单词]，否则记为新起点
                        if temp in words:
                            if temp not in hash_map:
                                hash_map[temp] = [r + 1]
                                r = next_r  # 不要忘记移动下标
                            else:
                                # 清除hash_map[当前单词]中所有不在窗口内的下标
                                while hash_map[temp] and hash_map[temp][0] < l:
                                    hash_map[temp].pop(0)
                                # 若当前单词还没出现足够次数，则直接加入
                                if len(hash_map[temp]) < target_count[temp]:
                                    hash_map[temp].append(r + 1)
                                    r = next_r  # 不要忘记移动下标
                                # 若当前单词已经出现了足够次数，则从第一次出现的地方的后一个单词开始窗口
                                else:
                                    l = hash_map[temp].pop(0) + step_length
                                    hash_map[temp].append(r + 1)
                                    r = next_r  # 不要忘记移动下标
                        else:
                            r = r + step_length
                            l = r + 1
                    else:
                        break
            hash_map.clear()  # 注意清空当次计数记录

        return ans


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    s = "barfoothefoobarman"
                    words = ["foo", "bar"]
                case 2:
                    # sample 2
                    s = "wordgoodgoodgoodbestword"
                    words = ["word", "good", "best", "word"]
                case 3:
                    # sample 3
                    s = "barfoofoobarthefoobarman"
                    words = ["bar", "foo", "the"]
                case 4:
                    # sample 4
                    s = "wordgoodgoodgoodbestword"
                    words = ["word", "good", "best", "good"]
                case 5:
                    # sample 5
                    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
                    words = ["fooo", "barr", "wing", "ding", "wing"]
                case 6:
                    # sample 6
                    s = "aaaaaaaaaaaaaa"
                    words = ["aa", "aa"]
                case 7:
                    # sample 6
                    s = "abaabaaa"
                    words = ["ba", "ab"]
                case _:
                    break
            print(f"ans = {solution.findSubstring(s,words)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
