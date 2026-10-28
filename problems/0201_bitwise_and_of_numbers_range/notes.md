# 201. Bitwise AND of Numbers Range

- 链接: https://leetcode.com/problems/bitwise-and-of-numbers-range/
- 难度: Medium
- 最优解:

## 题型
位运算

## 识别信号
- 求连续整数区间 [left, right] 所有数的按位与，right 可达 2^31 - 1，不能逐个相与
- 连续整数的低位会 0 / 1 交替出现，按位与之后这些位必然是 0

## 解题步骤
1. 暴力：从 left 到 right 逐个相与，O(right - left)；结果变成 0 时提前退出能救一部分，但像 [2^30, 2^31 - 1] 这种结果不为 0 的区间仍要跑约 10^9 次
2. 观察：某一位只要在区间里出现过 0，结果这一位就是 0；从 left 数到 right 的过程中，left 和 right 第一个不同的位以及它以下的所有位都一定出现过 0
3. 公共前缀：left、right 同时右移直到相等，记右移次数 s，答案是 left << s，O(log right)
4. 另一写法：当 left < right 时反复执行 right &= right - 1（消掉 right 最低位的 1），最后返回 right，O(log right)

## 关键一步
答案就是 left 和 right 二进制的公共前缀，后面补 0：从两者第一个不同的位开始往下，区间里每一位都出现过 0。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |

## 易错点
- left == right 时答案就是 left 本身
- left = 0 时答案一定是 0
- 用 right &= right - 1 时，循环条件是 left < right，不是 right > 0
