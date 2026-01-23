function maskEmail(email) {
    //mask
    //srdxchotu5@gmail.com --> s******5@gmail.com
    let maskedEmail = ""
    maskedEmail = email[0]
    let index = email.indexOf("@")
    let masks = "*".repeat(index - 2)
    maskedEmail += masks
    maskedEmail += email.slice(index - 1)
    return maskedEmail
}

const email = "soumyaranjan.bobby@gmail.com"
console.log(maskEmail(email))