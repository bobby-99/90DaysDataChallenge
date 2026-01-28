function bouncer(arr) {
    const falsy = [false, null, 0, "", undefined, NaN]
    let result = []
    for (let i in arr) {
        if (!falsy.includes(arr[i])) {
            result.push(arr[i])
        }
    }
    return result
}

console.log(bouncer([7, "ate", "", false, 9]))


// even better implementation
function bouncer(arr) {
    let result = [];
    for (let el of arr) {
        if (el) result.push(el);
    }
    return result;
}
