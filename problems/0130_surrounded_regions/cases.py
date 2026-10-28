METHOD = "solve"
CHECK_ARG = 0

CASES = [
    dict(args=([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']],), expected=[['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]),
    dict(args=([['X']],), expected=[['X']]),
    dict(args=([['X', 'X', 'X'], ['X', 'O', 'X'], ['X', 'X', 'X']],), expected=[['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]),
    dict(args=([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'X', 'O', 'X']],), expected=[['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'X', 'O', 'X']]),
    dict(args=([['O', 'X', 'X'], ['X', 'O', 'X'], ['X', 'X', 'X']],), expected=[['O', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]),
    dict(args=([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],), expected=[['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]),
    dict(args=([['O', 'X', 'O', 'O']],), expected=[['O', 'X', 'O', 'O']]),
]
