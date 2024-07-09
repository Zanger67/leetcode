/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var averageOfSubtree = function(root) {
    var counter = 0;
    function dfs(curr) {
        if (!curr) {
            return [0, 0];
        }
        let left = dfs(curr.left)
        let right = dfs(curr.right)
        let output = [left[0] + right[0] + curr.val, left[1] + right[1] + 1];

        if (curr.val == Math.floor(output[0] / output[1])) {
            counter++;
        }
        return output;
    }

    dfs(root);
    return counter;
};