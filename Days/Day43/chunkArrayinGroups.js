function chunkArrayInGroups(arr, num) {
    let result = [];
    for (let i = 0; i < arr.length; i += num) {
        let chunk = arr.slice(i, i + num)
        result.push(chunk)
    }
    return result
}

console.log(chunkArrayInGroups([1, 2, 3], 2))
console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2))
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4))
