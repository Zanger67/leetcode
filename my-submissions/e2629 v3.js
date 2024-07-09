var compose = function(functions) {
    
    return function(x) {
        functions.reverse().forEach(el => x = el(x));
        return x;
    }
};
