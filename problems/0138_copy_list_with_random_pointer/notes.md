# 138. Copy List with Random Pointer

- 链接: https://leetcode.com/problems/copy-list-with-random-pointer/
- 难度: Medium
- 最优解: 241225.py

## 题型
链表 · 哈希表

## 识别信号
- 深拷贝一个带 random 指针的链表，新链表不能指向原链表的任何节点
- random 可能指向后面还没复制的节点，需要"原节点 → 新节点"的对应关系

## 解题步骤
记 n = 链表长度。
1. 第一遍：按 next 顺序复制每个节点，用哈希表记录"原节点 → 新节点"
2. 第二遍：对每个原节点，通过哈希表找到它 random 指向节点的副本，接到新节点上
3. 两遍扫描，O(n) 时间、O(n) 哈希表
4. 省空间：把副本插在每个原节点后面（A → A' → B → B'），A'.random = A.random.next，最后再拆成两条链，额外空间 O(1)

## 关键一步
先建立"原节点 → 新节点"的映射，再统一连 random，这样 random 指向的节点一定已经存在。

## 各版本
| 文件 | 思路 | 时间 | 空间 | 结论 |
| --- | --- | --- | --- | --- |
| 241225.py | 第一遍复制 next 并用 id(原节点) 建映射，第二遍连 random | O(n) | O(n) | 通过，时间最优；额外空间可用穿插复制降到 O(1) |

## 易错点
- random 为 None 时副本的 random 也要是 None，不能去查映射
- 空链表直接返回 None
- 新链表的 random 必须指向副本，不能直接复制原节点的 random 指针
