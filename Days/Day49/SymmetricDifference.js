function destroyer(arr, ...rest) {
    const set = new Set(rest)
    return arr.filter(v => !set.has(v))
}

console.log(destroyer([1, 2, 3, 4, 2, 1], 1, 2))
console.log(destroyer(["pig", "hellcat", 'elephant', 'migrator pegion'], 'elephant', 'wolf'))
