function sumFibs(num) {
    let sum = 0;
    let a = 1, b = 1;

    while (a <= num) {
        if (a % 2 !== 0) {
            sum += a;
        }
        [a, b] = [b, a + b];
    }

    return sum;
}

console.log(sumFibs(100)); // 188