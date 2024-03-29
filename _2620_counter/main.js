/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    // Solution 2
    return function() {
        return n++;
    }


    // Solution 1
    // this.n = n;
    
    // return function() {
    //     this.n += 1;
    //     return this.n - 1;
    // };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */