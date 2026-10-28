# 35. Search Insert Position

- 链接: https://leetcode.com/problems/search-insert-position/
- 难度: Easy
- 最优解: 231107.py

## 题型
二分查找

## 识别信号
- 有序、无重复的数组，找 target 的下标或应插入的位置
- 题目明确要求 O(log n)

## 解题步骤
记 n = len(nums)。
1. 线性扫描：找第一个 ≥ target 的位置，O(n)
2. 优化：数组有序，二分查找"第一个 nums[i] ≥ target 的下标"（lower bound），O(log n)
3. 写法统一：left = 0、right = n（左闭右开），nums[mid] < target 时 left = mid + 1，否则 right = mid；循环结束时 left 就是答案，不需要特判剩一两个元素的情况

## 关键一步
插入位置就是"第一个 ≥ target 的下标"，二分到 left == right 时它就是答案。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |
| 231107.py | 二分，区间剩一个或两个元素时分情况直接返回 | O(log n) | O(1) | 最优 |

## 易错点
- target 比所有元素都大时返回 n（越过末尾）
- 231107.py 用"剩一个 / 剩两个元素"的特判避免死循环；写成标准 lower bound（左闭右开）可以去掉这些分支
- mid 写成 left + (right − left) // 2
