/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {

    // Solution 1
    let value = init;

    const increment = () => value += 1;
    const decrement = () => value -= 1;
    const reset = () => {
        value = init;
        return value;
    }


    return {
        increment,
        decrement,
        reset
    }


// Solution 2
//   return {
//     init: init,
//     value: init,
//     increment: function() {
//         return this.value += 1
//     },
//     decrement: function() {
//         return this.value -= 1
//     },
//     reset: function() {
//         this.value = this.init;
//         return this.value;
//     }
//   };

};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */