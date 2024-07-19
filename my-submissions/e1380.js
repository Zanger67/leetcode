/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers  = function(matrix) {
    const minRow = new Array(matrix.length);
    const maxCol = new Array(matrix[0].length);
    minRow.fill(Number.MAX_VALUE);
    maxCol.fill(0);

    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[0].length; c++) {
            if (matrix[r][c] < minRow[r])
                minRow[r] = matrix[r][c];
            if (matrix[r][c] > maxCol[c])
                maxCol[c] = matrix[r][c];
        }
    }

    const output = []
    for (x of minRow) {
        if (maxCol.includes(x))
            output.push(x);
    }

    return output;
};