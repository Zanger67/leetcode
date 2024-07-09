/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    return arr.flatMap((val, i) => fn(val, i) ? [val] : []);
};