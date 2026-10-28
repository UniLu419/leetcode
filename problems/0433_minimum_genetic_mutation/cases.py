METHOD = "minMutation"

CASES = [
    dict(args=('AACCGGTT', 'AACCGGTA', ['AACCGGTA'],), expected=1),
    dict(args=('AACCGGTT', 'AAACGGTA', ['AACCGGTA', 'AACCGCTA', 'AAACGGTA'],), expected=2),
    # 起点就是终点
    dict(args=('AACCGGTT', 'AACCGGTT', [],), expected=0),
    # 终点不在基因库
    dict(args=('AACCGGTT', 'AACCGGTA', [],), expected=-1),
    dict(args=('AAAAACCC', 'AACCCCCC', ['AAAACCCC', 'AAACCCCC', 'AACCCCCC'],), expected=3),
    # 基因库里含起点
    dict(args=('AACCGGTT', 'AACCGGTA', ['AACCGGTA', 'AACCGGTT'],), expected=1),
]
