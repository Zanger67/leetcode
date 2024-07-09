/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (this.length !== rowsCount * colsCount) {
        return [];
    }

    const output = [];
    for (let r = 0; r < rowsCount; r++) {
        output.push([]);
        for (let c = 0; c < colsCount; c++) {
            if (c % 2 == 0) {
                output[output.length - 1].push(this[c * rowsCount + r]);
            } else {
                output[output.length - 1].push(this[(c + 1) * rowsCount - r - 1]);
            }
        }
    }
    return output;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */