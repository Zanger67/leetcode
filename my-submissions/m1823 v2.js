/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function(n, k) {
    return (n == 1) ? 1 : (1 + (findTheWinner(n - 1, k) + k - 1) % n);
};