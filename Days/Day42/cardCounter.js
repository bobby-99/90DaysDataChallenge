let count = 0;
function cardCounter(card) {
    if ([2, 3, 4, 5, 6].includes(card)) {
        count += 1
    }
    else if ([7, 8, 9].includes(card)) {
        count = count
    }
    else if ([10, "J", "Q", "K", "A"].includes(card)) {
        count -= 1;
    }
    return count >= 1 ? `${count} Bet` : `${count} Hold`
}

console.log(cardCounter(8))