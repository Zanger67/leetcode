/**
 * @param {number} n
 * @param {number} time
 * @return {number}
 */
var passThePillow = function(n, time) {
    time %= 2 * (n - 1);
    if (time < n)
        return time + 1;
    time -= n - 1;
    return n - time;
};