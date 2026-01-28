function uniteUnique(...args) {
    let result = []
    for (let array of args) {
        for (let item of array) {
            if (!result.includes(item)) {
                result.push(item)
            }
        }
    }
    return result
}

uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1])