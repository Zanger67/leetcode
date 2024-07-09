/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    let obj = {
        toBe: function(n) {
            if (n !== val) throw new Error('Not Equal');
            return true;
        },
        notToBe: function(n) {
            if (val === n) throw new Error('Equal');
            return true;
        }
    }
    return obj;
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */