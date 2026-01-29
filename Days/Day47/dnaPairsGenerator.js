function pairElement(strands) {
    const dna = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    const pairedBases = []
    for (let char of strands) {
        const arr = [char, dna[char]]
        pairedBases.push(arr)
    }
    return pairedBases
}

pairElement("ATCGA")
