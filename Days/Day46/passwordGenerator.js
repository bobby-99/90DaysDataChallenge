function generatePassword(len) {
    const randomChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
    const lenOfChars = randomChars.length;
    let password = "";
    for (let i = 0; i < len; i++) {
        password += randomChars[Math.floor(Math.random() * lenOfChars)]
    }
    return password;
}

const password = generatePassword(8)
console.log(`Generated password: ${password}`)