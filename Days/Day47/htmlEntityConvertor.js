function convertHTML(string) {
    const entities = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&apos;"
    }
    let result = ""
    for (let char of string) {
        if (char in entities) {
            result += entities[char]
        } else {
            result += char
        }
    }
    return result
}



convertHTML("Dolce & Gabbana")