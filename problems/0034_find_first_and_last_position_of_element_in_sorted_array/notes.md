# 34. Find First and Last Position of Element in Sorted Array

- 链接: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- 难度: Medium
- 最优解:

## 题型
二分查找

## 识别信号
- 非递减数组（有重复），找 target 的第一个和最后一个位置，要求 O(log n)
- "第一个 ≥ x 的位置"（下界）一类的边界问题

## 解题步骤
记 n = len(nums)。
1. 暴力：线性扫描记录第一次和最后一次出现，O(n)
2. 二分找到任意一个 target 后向两侧线性扩展：target 重复很多次时退化成 O(n)
3. 两次二分：写一个 lower(x) 返回第一个 ≥ x 的下标；起点 = lower(target)，若越界或 nums[起点] != target 就返回 [-1, -1]；终点 = lower(target + 1) − 1；O(log n) 时间、O(1) 空间

## 关键一步
第一个位置 = 第一个 ≥ target 的下标，最后一个位置 = 第一个 ≥ target + 1 的下标 − 1，两个都用同一个下界二分。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |

## 易错点
- lower 的搜索区间取 [0, n)，结果可能等于 n（所有数都小于 x），读 nums[i] 之前要先判断 i < n
- 空数组直接返回 [-1, -1]
- 只有一个 target 时起点和终点相同
- 全部都是 target 时"二分后向两侧扩展"会退化成 O(n)
