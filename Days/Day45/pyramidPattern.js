function pyramid(char, rows, bool) {
    if (bool === false) {
        return trianglePyramid(char, rows)
    }
    return reversePyramid(char, rows)
}

function trianglePyramid(char, rows) {
    let result = "\n"
    let chars = 1
    for (let i = 0; i < rows; i++) {
        result += " ".repeat(rows - (i + 1))
        // for(let j = 1; j < rows; j++){
        //   result += char.repeat()
        // }
        result += char.repeat(chars)
        chars += 2
        result += "\n"
    }
    return result
}

function reversePyramid(char, rows) {
    let result = "\n"
    let chars = rows + (rows - 1)
    for (let i = 0; i < rows; i++) {
        result += " ".repeat(i)
        result += char.repeat(chars)
        chars -= 2
        result += "\n"
    }
    return result
}

console.log(pyramid("o", 5, false))