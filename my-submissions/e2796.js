/**
 * @param {number} times
 * @return {string}
 */
String.prototype.replicate = function(times) {
    if (times === 1) {
        return this;
    }
    let half = this.replicate(Math.floor(times / 2));
    return half + half + (times % 2 == 1 ? this : '');
}