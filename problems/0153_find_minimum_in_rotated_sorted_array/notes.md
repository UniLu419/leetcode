# 153. Find Minimum in Rotated Sorted Array

- 链接: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- 难度: Medium
- 最优解:

## 题型
二分查找

## 识别信号
- 升序且互不相同的数组被旋转过，求最小值，要求 O(log n)
- 最小值就是旋转点：它左边一段整体大于右边一段

## 解题步骤
记 n = len(nums)。
1. 暴力：直接 min(nums) 或线性扫描找下降点，O(n)
2. 二分：lo = 0，hi = n − 1；比较 nums[mid] 和 nums[hi]：nums[mid] > nums[hi] 说明最小值在 mid 右侧，lo = mid + 1；否则 [mid, hi] 有序，最小值在 mid 或它左边，hi = mid；lo == hi 时 nums[lo] 就是答案；O(log n) 时间、O(1) 空间

## 关键一步
和区间右端点比较：nums[mid] > nums[hi] 说明旋转点在 (mid, hi] 里，否则 [mid, hi] 是有序的，最小值在 lo..mid 之间。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |

## 易错点
- 和 nums[hi] 比较，不要和 nums[lo] 比较：数组没旋转时，和 nums[lo] 比判断不出最小值在哪边
- 收缩右端用 hi = mid，不是 mid − 1，mid 自己可能就是最小值
- 循环条件 lo < hi
- 数组可能没有旋转（旋转 n 次），长度可能为 1
