# Booking: Shift Strings

- 链接:
- 难度:
- 最优解: 241210.js

## 题型
字符串模拟 · 数学

## 识别信号
- 题目（HackerRank，Booking 面试题）：一次左移把首字符移到末尾，一次右移把末字符移到开头。对字符串 s 先做 leftShifts 次左移、再做 rightShifts 次右移，返回结果
- 左移和右移互相抵消，移动 len(s) 次回到原样，用取模算净位移

## 解题步骤
记 n = len(s)。
1. 暴力：逐次模拟每一次移位，O((leftShifts + rightShifts)·n)
2. 瓶颈：左右移位可以抵消，且每 n 次一个循环
3. 优化：净左移量 = (leftShifts − rightShifts) mod n，结果就是 s[净左移量:] + s[:净左移量]，O(n)

## 关键一步
把所有移位合成一次净左移 (leftShifts − rightShifts) mod n，再切片拼接。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |
| 241210.js | JavaScript，净位移取模，负数加 n 调成非负，再 slice 拼接 | O(n) | O(n) | 最优（工具不运行 JS） |

## 易错点
- JavaScript 的 % 对负数返回负数，要加上 n 调成非负（241210.js 已处理）；Python 的 % 本身就非负
- 移位次数可能远大于 len(s)，先取模
