/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var cnt = n - 1;
    return function() {
        cnt++;
        return cnt;
    };
};
