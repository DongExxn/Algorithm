const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");
const n = parseInt(input[0]);
const board = input.slice(1).map((line) => line.split(""));

function maxCandy(board) {
  const n = board.length;
  let maxCount = 0;

  function countMax() {
    let maxLength = 0;
    for (let i = 0; i < n; i++) {
      let rowCount = 1;
      let colCount = 1;
      for (let j = 1; j < n; j++) {
        if (board[i][j] === board[i][j - 1]) {
          rowCount++;
        } else {
          maxLength = Math.max(maxLength, rowCount);
          rowCount = 1;
        }
        if (board[j][i] === board[j - 1][i]) {
          colCount++;
        } else {
          maxLength = Math.max(maxLength, colCount);
          colCount = 1;
        }
      }
      maxLength = Math.max(maxLength, rowCount, colCount);
    }
    return maxLength;
  }

  function swapCheck(i, j, ni, nj) {
    if (board[i][j] !== board[ni][nj]) {
      [board[i][j], board[ni][nj]] = [board[ni][nj], board[i][j]];
      maxCount = Math.max(maxCount, countMax());
      [board[i][j], board[ni][nj]] = [board[ni][nj], board[i][j]];
    }
  }

  maxCount = countMax();

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i + 1 < n) swapCheck(i, j, i + 1, j);
      if (j + 1 < n) swapCheck(i, j, i, j + 1);
    }
  }

  return maxCount;
}

console.log(maxCandy(board));
