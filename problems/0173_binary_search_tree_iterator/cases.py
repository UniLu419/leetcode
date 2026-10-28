from helpers import build_tree

CLASS = "BSTIterator"

CASES = [
    dict(ops=['BSTIterator', 'next', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext'], args=[[build_tree([7, 3, 15, None, None, 9, 20])], [], [], [], [], [], [], [], [], []], expected=[None, 3, 7, True, 9, True, 15, True, 20, False]),
    dict(ops=['BSTIterator', 'hasNext', 'next', 'hasNext'], args=[[build_tree([1])], [], [], []], expected=[None, True, 1, False]),
    dict(ops=['BSTIterator', 'next', 'next', 'next', 'hasNext'], args=[[build_tree([3, 2, None, 1])], [], [], [], []], expected=[None, 1, 2, 3, False]),
    dict(ops=['BSTIterator', 'hasNext', 'next', 'next', 'hasNext', 'next', 'hasNext'], args=[[build_tree([0, None, 5, None, 1000000])], [], [], [], [], [], []], expected=[None, True, 0, 5, True, 1000000, False]),
]
