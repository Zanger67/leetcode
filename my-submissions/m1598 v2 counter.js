/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    var counter = 0;

    logs.forEach(el => {
        switch (el) {
        case './' :
            break;
        case '../' :
            if (counter > 0)
                counter--;
            break;
        default :
            counter++;
            break;
        }
    });

    return counter;
};