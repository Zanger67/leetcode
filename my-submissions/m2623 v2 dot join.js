/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const mapRef = {};
    return function(...args) {
        const key = args.join(',');
        if (!(key in mapRef)) {
            mapRef[key] = fn(...args);
        }
        return mapRef[key];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */