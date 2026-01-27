function fearNotLetter(str) {
    for (let i = 0; i < str.length - 1; i++) {
        const currentChar = str.charCodeAt(i)
        const nextChar = str.charCodeAt(i + 1)
        if (nextChar === currentChar + 1) {
            continue
        }
        return String.fromCharCode(currentChar + 1)
    }
    return undefined
}

fearNotLetter("bcdef")