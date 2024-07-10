/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    const stk = [];

    logs.forEach(el => {
        switch (el) {
        case './' :
            break;
        case '../' :
            stk.pop();
            break;
        default :
            stk.push(el);
            break;
        }
    });

    return stk.length;
};