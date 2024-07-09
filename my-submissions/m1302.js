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
var deepestLeavesSum = function(root) {
    var deepestDepth = 0;
    var output = 0;
    
    function dfs(curr, currDepth) {
        if (curr == undefined) {
            return;
        }
        if (currDepth > deepestDepth) {
            deepestDepth = currDepth;
            output = 0;
        }
        if (currDepth == deepestDepth) {
            output += curr.val;
        }
        currDepth++;
        dfs(curr.left, currDepth)
        dfs(curr.right, currDepth)
    }
    dfs(root, 0);
    return output;
};