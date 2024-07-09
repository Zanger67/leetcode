/**
 * @param {number} n
 * @return {string[]}
 */
var validStrings = function(n) {
    const outputs = [];

    function propogate(curr, r) {
        if (r === 0) {
            outputs.push(curr.join(''));
            return;
        }

        if (r == 1) {
            outputs.push(curr.join('') + '0');
            outputs.push(curr.join('') + '1');
            return;
        }

        curr.push('1');
        propogate(curr, r - 1);
        curr.pop();
        curr.push('01');
        propogate(curr, r - 2);
        curr.pop();
    }

    propogate([], n);
    return outputs;
};