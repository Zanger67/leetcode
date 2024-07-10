class helper {
    constructor(val) {
        this.val = val;
    }

    toBe(n) {
        if (n !== this.val) throw new Error('Not Equal');
        return true;
    }

    notToBe(n) {
        if (n === this.val) throw new Error('Equal');
        return true;
    }
}


/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return new helper(val);
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */