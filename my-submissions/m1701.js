/**
 * @param {number[][]} customers
 * @return {number}
 */
var averageWaitingTime = function(customers) {
    var output = 0;
    var currentTime = 0;

    function cust(customer) {
        if (customer[0] > currentTime) {
            currentTime = customer[0];
        }

        output += (currentTime + customer[1]) - customer[0];
        currentTime += customer[1];
    }

    customers.forEach(cust);
    return output / customers.length;
};