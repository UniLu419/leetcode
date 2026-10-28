# 28. Find the Index of the First Occurrence in a String

- 链接: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
- 难度: Easy
- 最优解: 231107_2.py

## 题型
字符串模拟

## 识别信号
- 在主串里找模式串第一次出现的位置，找不到返回 -1
- 只有两个字符串、没有其他条件，就是标准的字符串匹配

## 解题步骤
记 n = len(haystack)，m = len(needle)。
1. 暴力：枚举起点 i 从 0 到 n − m，比较 haystack[i : i + m] 和 needle，O((n − m + 1)·m)
2. 瓶颈：失配后起点只右移一位，已经比较过的字符信息全部丢掉
3. 优化：KMP。先算 needle 每个前缀的"最长相等真前后缀"长度；失配时模式串回退到这个长度继续比，主串指针不后退，O(n + m)

## 关键一步
失配时利用 needle 已匹配部分的最长相等前后缀，直接把模式串对齐过去继续比较，主串指针不回头。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |
| 231107.py | 直接调用 haystack.find(needle) | 取决于库实现 | O(1) | 通过，调库，没有自己实现匹配 |
| 231107_2.py | 枚举起点，切片与 needle 比较 | O((n − m + 1)·m) | O(m) | 通过，未达最优（KMP 为 O(n + m)） |

## 易错点
- 起点最大是 n − m，range 要写 n − m + 1：原注释"注意这里的边界需要+1"
- needle 比 haystack 长时 range 为空，直接返回 -1
