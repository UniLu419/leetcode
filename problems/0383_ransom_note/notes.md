# 383. Ransom Note

- 链接: https://leetcode.com/problems/ransom-note/
- 难度: Easy
- 最优解: 241218_2.py

## 题型
哈希计数

## 识别信号
- magazine 里每个字母只能用一次，判断能否拼出 ransomNote，即比较两边每个字母的出现次数
- 只关心次数、不关心顺序

## 解题步骤
记 m = len(ransomNote)，n = len(magazine)。
1. 暴力：对 ransomNote 的每个字母在 magazine 里找一个未用过的同字母并标记，O(m·n)
2. 瓶颈：每次都在 magazine 里线性查找
3. 优化：先统计 magazine 的字母次数，再统计 ransomNote 的字母次数，每个字母都要求 magazine 的次数 ≥ ransomNote 的次数，O(m + n)

## 关键一步
能拼出等价于：ransomNote 中每个字母的次数都不超过它在 magazine 中的次数。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |
| 241218.py | 先数 magazine，再遍历 ransomNote 边计数边比较，不够就提前返回 | O(m + n) | O(字符集大小) | 通过 |
| 241218_2.py | 两边都数完，再遍历 ransomNote 的键统一比较 | O(m + n) | O(字符集大小) | 最优，大输入略快于上一版 |

## 易错点
- 字母在 magazine 里根本没出现时要单独判断（key not in hash_map_m），否则直接取值会 KeyError
- 原注释"hash完后统一判断快一点"：两版复杂度相同，后一版循环里少了比较
