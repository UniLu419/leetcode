grid = [[1, 1, 1], [0, 0, 1], [2, 3, 4]]
pricing = [2, 3]
start = [0, 0]
k = 3
row = 2
col = 0
row_length = len(grid)
col_length = len(grid[0])
current_row = start[0] + row
current_col = start[1] + col
if current_row < row_length and current_col < col_length:
    if (
        grid[current_row][current_col] >= pricing[0]
        and grid[current_row][current_col] <= pricing[1]
    ):
        print([current_row, current_col])
