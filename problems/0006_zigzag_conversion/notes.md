# 6. Zigzag Conversion

- 链接: https://leetcode.com/problems/zigzag-conversion/
- 难度: Medium
- 最优解: 241214.py

## 题型
字符串模拟 · 数学

## 识别信号
- 按固定规则把字符"摆"成图形，再按行读出，属于模拟
- 摆放是周期性的：竖着向下 numRows 个、斜着向上 numRows − 2 个，可以用取余直接算出每个字符落在哪一行

## 解题步骤
记 n = len(s)，k = numRows，周期 step = 2k − 2。
1. 直接模拟：开一个 k 行的二维网格，按之字形逐格填字符，再逐行读出；网格有大量空格，浪费空间
2. 观察：只关心每个字符在哪一行，列的位置不影响结果
3. 优化：每一行维护一个字符串；第 i 个字符的行号由 i mod step 决定，O(n)
4. 特判 k = 1：周期为 0 不能取余，直接返回原串

## 关键一步
周期 step = 2·numRows − 2；余数 r = i mod step，r < numRows 时行号是 r，否则行号是 step − r。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |
| 231107.java | Java，逐行输出：第 i 行取下标 i、i + step、i + 2·step…，中间行再补上每个周期斜线上的 j − 2i + step | O(n²)（单个 String 反复用 + 拼接，每次复制整串） | O(n) | 未达最优（Java 版工具不运行），拼接改用 StringBuilder 即为 O(n) |
| 241214.py | 每行一个字符串，用 i mod step 算出行号后追加，最后 join | O(n)，另加每行字符串追加时的复制 | O(n) | 最优 |

## 易错点
- numRows = 1 时周期为 0，必须先特判；241214.py 用 numRows < 2 判断，原注释："首先返回不需处理的字符串"
- numRows 不小于字符串长度时（"ABC"，5）结果就是原串，取余公式自然成立
- 判断前半周期的条件是 余数 + 1 ≤ numRows，即 余数 < numRows；写成 ≤ numRows 会把斜线上的字符放错行
