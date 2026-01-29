function dropElements(arr, func) {
    const fun = func;
    for (let i = 0; i <= arr.length; i++) {
        if (fun(arr[i])) {
            return arr.slice(i)
        }
    }
    return [];
}

console.log(dropElements([0, 1, 0, 1], function (n) { return n === 1; }))