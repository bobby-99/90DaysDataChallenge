function findLongestWordLength(sentence) {
    let max = 0;
    const words = sentence.trim().split(" ");

    for (let word of words) {
        if (word !== "" && word.length > max) {
            max = word.length;
        }
    }

    return max;
}
