# 380. Insert Delete GetRandom O(1)

- 链接: https://leetcode.com/problems/insert-delete-getrandom-o1/
- 难度: Medium
- 最优解: 241214_2.py

## 题型
设计 · 哈希表

## 识别信号
- 要求 insert、remove、getRandom 都是平均 O(1)
- 哈希表能 O(1) 增删查，但不能 O(1) 等概率随机取；数组能 O(1) 随机取，但不能 O(1) 删除中间元素，需要把两者结合

## 解题步骤
记 n 为当前集合大小。
1. 直接用集合：insert/remove 是 O(1)，但 getRandom 要先把集合转成列表再随机，O(n)
2. 瓶颈：随机取需要按下标访问的连续存储
3. 优化：数组存值、哈希表存"值 → 在数组中的下标"；删除时把数组最后一个元素搬到被删位置并更新它的下标，再弹出末尾，三个操作都是 O(1)

## 关键一步
删除中间元素时，用数组末尾元素覆盖被删位置、更新末尾元素在哈希表里的下标，再 pop 末尾，避免数组整体移位。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |
| 241214.py | 只用 set；getRandom 时 list(set) 再 random.choice | insert/remove O(1)，getRandom O(n) | O(n) | 通过，getRandom 未达 O(1) |
| 241214_2.py | 列表存值 + 哈希表存值 → 下标，删除时与末尾元素交换后 pop | 均为 O(1) | O(n) | 最优 |

## 易错点
- 插入时下标就是追加前的 len(list)：原注释"len = index+1"
- 删除时先写入 hash_map[末尾值] = 被删下标，再 pop(val)：被删的正好是末尾元素时，顺序反了会把已删除的值重新写回哈希表
- 241214_2.py 里 last_index 存的其实是末尾元素的值，不是下标
