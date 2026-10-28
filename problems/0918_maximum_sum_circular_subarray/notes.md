# 918. Maximum Sum Circular Subarray

- 链接: https://leetcode.com/problems/maximum-sum-circular-subarray/
- 难度: Medium
- 最优解:

## 题型
动态规划

## 识别信号
- 53 题（最大子数组和）的环形版本：子数组可以从尾部绕回头部，但每个元素最多用一次
- 绕过首尾的子数组 = 整个数组去掉中间连续的一段

## 解题步骤
记 n = len(nums)，total = sum(nums)。
1. 暴力：枚举起点 i 和长度 1..n，下标取 (i + j) % n 累加，O(n²)
2. 瓶颈：每个起点都重新累加
3. 分两种情况：不跨首尾时就是普通最大子数组和，用 53 题的 Kadane 求 maxSum；跨首尾时选中的是一段前缀加一段后缀，等于 total − 中间某段连续子数组的和，中间那段要最小，同一遍扫描用 Kadane 求最小子数组和 minSum；O(n) 时间、O(1) 空间
4. 特判：全部为负数时 minSum = total，total − minSum = 0 对应空子数组，不合法，此时答案是 maxSum；否则答案是 max(maxSum, total − minSum)

## 关键一步
跨首尾的子数组 = 整个数组去掉中间一段，所以它的最大和 = total − 最小子数组和；再和不跨首尾的最大子数组和取较大者。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |

## 易错点
- 全是负数时 total − minSum 等于 0（空子数组），必须返回 maxSum，可用 maxSum < 0 判断
- 把数组复制成两倍直接跑 Kadane 不对：选出的长度可能超过 n，同一个元素被用两次
- maxSum 和 minSum 的初值用 nums[0]，不要用 0
