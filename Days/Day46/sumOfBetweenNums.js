function sumAll(arr) {
    const { first, last } = getSmallLarge(arr)
    // const sumOffirst = (first * (first + 1)) / 2
    // const sumOflast = ((last * (last + 1)) / 2) - sumOffirst + 1
    // return sumOflast
    return (((last + 1) * last) - (first * (first - 1))) / 2
}

function getSmallLarge([a, b]) {
    return a < b ? { first: a, last: b } : { first: b, last: a };
}

console.log(sumAll([5, 10]))