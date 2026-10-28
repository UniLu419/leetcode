# 错题本

由 `python3 lc.py` 根据 mistakes/ 里的每条记录生成；改记录后运行 `python3 lc.py mistakes` 即可更新。

## Python 用法（2）

### 2026-10-28 · [1. Two Sum](problems/0001_two_sum/notes.md)

记录原文: [mistakes/2026-10-28_0001_two_sum_2.md](mistakes/2026-10-28_0001_two_sum_2.md)

**错在哪**

第 13 行写成 `hash_table[nums[i]] = hash_table[nums[i]].append(i)`。`append` 是原地修改、返回 None，赋值回去就把这个值的下标列表换成了 None。同一个数第二次出现后（如 [3,3]、[0,4,3,0]），第 19 行 `len(hash_table[ans])` 会报 `TypeError: object of type 'NoneType' has no len()`。

**正确写法**

```python
hash_table[nums[i]].append(i)
```

**知识点**

- 原地修改的方法都返回 None：`list.append / extend / insert / sort / reverse`、`dict.update`、`set.add` 等，不要把它们的结果赋值回去。
- 需要返回新对象时用 `sorted(x)`、`x + [i]` 这类写法。
- "值 → 列表"的字典可以写成 `d.setdefault(key, []).append(i)`，或用 `collections.defaultdict(list)`，省掉先判断再建列表这一步。

### 2026-10-28 · [1. Two Sum](problems/0001_two_sum/notes.md)

记录原文: [mistakes/2026-10-28_0001_two_sum.md](mistakes/2026-10-28_0001_two_sum.md)

**错在哪**

第 12 行用 `hash_table[nums[i]] is not None` 判断某个值有没有存过。键还不在字典里时，`hash_table[nums[i]]` 这一步就直接抛 KeyError，根本走不到 `is not None` 的比较，所以 5 个样例全部在这一行报错。

**正确写法**

```python
if nums[i] in hash_table:
```

**知识点**

- `d[key]` 取不存在的键会抛 KeyError，不会返回 None。
- 判断键在不在用 `key in d`；想取值、不存在时给默认值用 `d.get(key)` 或 `d.get(key, 默认值)`。
