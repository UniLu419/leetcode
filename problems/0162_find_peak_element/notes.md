# 162. Find Peak Element

- 链接: https://leetcode.com/problems/find-peak-element/
- 难度: Medium
- 最优解:

## 题型
二分查找

## 识别信号
- 要求 O(log n)，但数组整体无序
- 相邻元素一定不相等，且两端外侧视为 −∞：只看 nums[mid] 和 nums[mid + 1] 的大小就能断定哪一侧一定有峰

## 解题步骤
记 n = len(nums)。
1. 暴力：从左往右扫，第一个满足 nums[i] > nums[i + 1] 的 i 就是峰（它左边一路上升）；都不满足则 n − 1 是峰；O(n)
2. 瓶颈：题目要求 O(log n)
3. 二分：lo = 0，hi = n − 1；若 nums[mid] < nums[mid + 1]，mid 右侧一定有峰，lo = mid + 1；否则 mid 或它左侧一定有峰，hi = mid；lo == hi 时就是一个峰；O(log n) 时间、O(1) 空间

## 关键一步
沿上坡方向走一定能走到峰：nums[mid] < nums[mid + 1] 时一直向右，要么中途开始下降（那里就是峰），要么升到最右端（右侧是 −∞，也是峰）。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |

## 易错点
- 用 lo < hi 和 hi = mid 的写法，mid 总小于 hi，访问 nums[mid + 1] 不会越界
- 峰可能有多个，返回任意一个都对
- nums[i] 可以等于 −2^31，不要拿 −2^31 当边界哨兵，用 float('-inf') 或直接判断下标
- 长度为 1 时答案是 0
