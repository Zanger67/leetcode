/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var origInit = init;
    obj = {
        increment: function() {
            return ++init;
        },

        decrement: () => --init,
        
        reset: function() {
            init = origInit;
            return init;
        }
    }
    return obj;
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */