function mutation(arr) {
    const first = arr[0].toLowerCase()
    const second = arr[1].toLowerCase()
    for (const char of second) {
        if (first.includes(char)) {
            continue;
        } else {
            return false
        }
    }
    return true
}

console.log(mutation(["Alien", "line"]))
console.log(mutation(["Hello", "hey"]))