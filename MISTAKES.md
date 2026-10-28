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

**`is not None` 的用法**

- `x is not None` 只判断"x 这个值是不是 None"，前提是 x 已经顺利取到了。它不能用来判断"字典里有没有这个键"——取值那一步就会先报错。
- 和 `d.get` 搭配可以不报错：`if d.get(key) is not None:`。但如果字典里本来就存了 None（`d = {"a": None}`），它会误判成"没有这个键"，所以判断键是否存在还是用 `in`。
- 比较 None 用 `is` / `is not`，不用 `==` / `!=`：None 只有一个对象，`is` 比的是"是不是同一个对象"，不会被类里自定义的 `__eq__` 干扰；这也是 PEP 8 的规定。
- `if x is not None:` 和 `if x:` 不一样：`if x:` 会把 `0`、`""`、`[]`、`{}` 也当成"没有"。下标 0、空列表都是合法值时，要用 `is not None`。

  ```python
  i = d.get(key)     # 下标，可能是 0
  if i:              # 错：i == 0 时也进不来
  if i is not None:  # 对：只排除"没取到"
  ```

- 刷题里最常用的场景：链表、树的节点判空（`while node is not None:`，常简写成 `while node:`，因为节点对象本身总是真值），以及函数可能返回 None 的结果（如 `d.get`、`re.match`）。
