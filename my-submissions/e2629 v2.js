var compose = function(functions) {
    
    return function(x) {
        output = x
        functions.reverse().forEach(el => output = el(output));
        return output;
    }
};