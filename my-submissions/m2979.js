/**
 * @param {number} primeOne
 * @param {number} primeTwo
 * @return {number}
 */
var mostExpensiveItem = function(primeOne, primeTwo) {
    return primeOne * primeTwo - primeOne - primeTwo;
};