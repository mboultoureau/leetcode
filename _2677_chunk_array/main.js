/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    if (arr.length === 0) return [];
    if (arr.length <= size) return [arr];

    const chunkedArray = [];
    let current = [];

    arr.forEach((item, index) => {
        current.push(item);
        if (index === arr.length - 1 || current.length === size) {
            chunkedArray.push(current);
            current = [];
        }
    })

    return chunkedArray;
};
