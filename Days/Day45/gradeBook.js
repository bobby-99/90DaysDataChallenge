function getAverage(arr) {
    let sum = 0;
    for (let el of arr) {
        sum += el
    }
    return sum / arr.length
}

function getGrade(score) {
    if (score === 100) {
        return "A+"
    } else if (score >= 90 && score < 100) {
        return "A"
    } else if (score >= 80 && score < 90) {
        return "B"
    } else if (score >= 70 && score < 80) {
        return "C"
    } else if (score >= 60 && score < 70) {
        return "D"
    } else {
        return "F"
    }
}

function hasPassingGrade(score) {
    return "F" !== getGrade(score)
}

function studentMsg(arr, score) {
    const avg = getAverage(arr);
    const grade = getGrade(score);

    // learnt storing of function values beforehand to use them as many times as one can

    if (grade !== "F") {
        return `Class average: ${avg}. Your grade: ${grade}. You passed the course.`;
    } else {
        return `Class average: ${avg}. Your grade: ${grade}. You failed the course.`;
    }
}


console.log(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]))
console.log(getGrade(89))
console.log(hasPassingGrade(59))