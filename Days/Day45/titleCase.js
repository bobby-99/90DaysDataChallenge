function titleCase(str) {
    let result = ""
    let arr = str.split(" ")
    for (let char of arr) {
        result += char[0].toUpperCase() + char.slice(1).toLowerCase() + " "
    }
    return result.trimEnd()
}

console.log(titleCase("I'm a little tea pot"))
console.log(titleCase("HERE IS MY HANDLE HERE IS MY SPOUT"))
console.log(titleCase("sHoRt AnD sToUt"))
