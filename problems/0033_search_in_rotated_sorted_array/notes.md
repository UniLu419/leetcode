# 33. Search in Rotated Sorted Array

- 链接: https://leetcode.com/problems/search-in-rotated-sorted-array/
- 难度: Medium
- 最优解:

## 题型
二分查找

## 识别信号
- 有序数组在某个位置被旋转过，元素互不相同，要求 O(log n)
- 从任意位置切开，左右两段至少有一段是有序的

## 解题步骤
记 n = len(nums)。
1. 暴力：线性扫描找 target，O(n)
2. 两次二分：先二分找到最小值的位置（即旋转点，153 题），把数组分成两段有序区间，再判断 target 落在哪一段、在那段里二分；O(log n)
3. 一次二分：每次取 mid，用 nums[lo] <= nums[mid] 判断左半 [lo, mid] 是否有序；若有序且 nums[lo] <= target < nums[mid]，就去左半，否则去右半；左半无序时右半 [mid, hi] 必有序，同理判断；O(log n) 时间、O(1) 空间

## 关键一步
mid 把区间分成两半，其中一半一定有序；只在有序那一半里用两端的值判断 target 在不在，在就进去，不在就去另一半。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |

## 易错点
- 判断左半有序要写 nums[lo] <= nums[mid]，带等号：lo == mid 时左半只有一个元素，也算有序
- 范围判断的开闭：左半有序时是 nums[lo] <= target < nums[mid]，右半有序时是 nums[mid] < target <= nums[hi]
- 数组可能没有旋转，长度可能为 1
- 先判断 nums[mid] == target 再缩区间
