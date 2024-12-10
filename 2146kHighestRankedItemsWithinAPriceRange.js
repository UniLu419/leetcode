/**
 * @param {number[][]} grid
 * @param {number[]} pricing
 * @param {number[]} start
 * @param {number} k
 * @return {number[][]}
 * 不知道哪有毛病，之后再看
 */
var highestRankedKItems = function (grid, pricing, start, k) {
  const rowLength = grid.length;
  const colLength = grid[0].length;
  const distance = []
  for (let i = 0; i < rowLength; i++) {
    let tempRow = [];
    for (let j = 0; j < colLength; j++) {
        tempRow.push(-1);
    }
    distance.push(tempRow);
}
  distance[start[0]][start[1]] = 0;
  const queue = [start];
  const cells = [];
  let currentDistance = 0;
  if (
    grid[start[0]][start[1]] >= pricing[0] &&
    grid[start[0]][start[1]] <= pricing[1]
  ) {
    cells.push(start);
  }
  while (queue.length > 0) {
    const current = queue.splice(0, 1)[0];
    const row = current[0];
    const col = current[1];
    if (currentDistance < distance[row][col] && cells.length >= k) {
      break;
    }
    currentDistance = distance[row][col];
    if (row - 1 >= 0) {
      if (grid[row - 1][col] != 0 && distance[row - 1][col] == -1) {
        distance[row - 1][col] = currentDistance + 1;
        queue.push([row - 1, col]);
        if (
          grid[row - 1][col] >= pricing[0] &&
          grid[row - 1][col] <= pricing[1]
        )
          cells.push([row - 1, col]);
      }
    }
    if (col - 1 >= 0) {
      if (grid[row][col - 1] != 0 && distance[row][col - 1] == -1) {
        distance[row][col - 1] = currentDistance + 1;
        queue.push([row, col - 1]);
        if (
          grid[row][col - 1] >= pricing[0] &&
          grid[row][col - 1] <= pricing[1]
        )
          cells.push([row, col - 1]);
      }
    }
    if (row + 1 < rowLength) {
      if (grid[row + 1][col] != 0 && distance[row + 1][col] == -1) {
        distance[row + 1][col] = currentDistance + 1;
        queue.push([row + 1, col]);
        if (
          grid[row + 1][col] >= pricing[0] &&
          grid[row + 1][col] <= pricing[1]
        )
          cells.push([row + 1, col]);
      }
    }
    if (col + 1 < colLength) {
      if (grid[row][col + 1] != 0 && distance[row][col + 1] == -1) {
        distance[row][col + 1] = currentDistance + 1;
        queue.push([row, col + 1]);
        if (
          grid[row][col + 1] >= pricing[0] &&
          grid[row][col + 1] <= pricing[1]
        )
          cells.push([row, col + 1]);
      }
    }
    cells.sort((a, b) => {
        const [aRow, aCol] = a;
        const [bRow, bCol] = b;
        // 先比较distance的值
        if (distance[aRow][aCol] < distance[bRow][bCol]) {
            return -1;
        }
        if (distance[aRow][aCol] > distance[bRow][bCol]) {
            return 1;
        }
        // 如果distance的值相等，比较grid的值
        if (grid[aRow][aCol] < grid[bRow][bCol]) {
            return -1;
        }
        if (grid[aRow][aCol] > grid[bRow][bCol]) {
            return 1;
        }
        // 如果grid的值也相等，比较行坐标aRow和bRow
        if (aRow < bRow) {
            return -1;
        }
        if (aRow > bRow) {
            return 1;
        }
        // 如果行坐标也相等，比较列坐标aCol和bCol
        if (aCol < bCol) {
            return -1;
        }
        if (aCol > bCol) {
            return 1;
        }
        // 如果所有条件都相等，返回0，表示它们顺序无先后之分
        return 0;
    });
    return cells.length <= k ? cells : cells.slice(0, k);
  }
};
