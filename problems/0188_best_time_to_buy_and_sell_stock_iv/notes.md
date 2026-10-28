# 188. Best Time to Buy and Sell Stock IV

- 链接: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
- 难度: Hard
- 最优解:

## 题型
动态规划

## 识别信号
- 买卖股票，最多完成 k 笔交易，手上最多持有一股（123 题"最多两笔"的推广）
- 状态可以用"已经做到第几笔交易 + 现在是否持有股票"完整描述

## 解题步骤
记 n = len(prices)。
1. 暴力：每天枚举买入 / 卖出 / 不动，指数级
2. 动态规划：dp[j][i] = 前 i 天内最多 j 笔交易的最大利润 = max(dp[j][i−1], max over m < i of (prices[i] − prices[m] + dp[j−1][m]))，O(k·n²) 时间
3. 瓶颈：内层对 m 取最大值时每次都重扫；随着 i 增大，只需维护 best = max(dp[j−1][m] − prices[m])，O(k·n) 时间、O(k·n) 空间
4. 状态机写法：buy[j]、sell[j] 表示完成第 j 次买入后、第 j 次卖出后的最大余额，记 p = 当天价格，每天对 j = 1..k 更新 buy[j] = max(buy[j], sell[j−1] − p)、sell[j] = max(sell[j], buy[j] + p)，sell[0] = 0；答案 sell[k]，O(n·k) 时间、O(k) 空间
5. 剪枝：k ≥ n // 2 时次数限制不起作用，等价于不限次数（122 题），把所有相邻上涨差价相加即可，O(n)

## 关键一步
第 j 次买入的成本从"完成 j−1 笔交易后的最大利润"里扣：buy[j] = max(buy[j], sell[j−1] − price)，于是 k 笔交易就是把 123 题的两组状态扩成 k 组。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |

## 易错点
- buy 初值是负无穷（或 −prices[0]），sell 初值是 0
- k 远大于 n / 2 时按 k 开数组是浪费，直接用不限次数的贪心
- 只有一天时利润为 0
- 同一天对同一个 j 先更新 buy[j] 再更新 sell[j] 没有问题：同天买卖收益为 0
