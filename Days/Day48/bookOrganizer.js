const books = [
    {
        title: "Your Next Five Moves",
        authorName: "Patrick Bet-David",
        releaseYear: 2020
    },
    {
        title: "Atomic Habits",
        authorName: "James Clear",
        releaseYear: 2018
    },
    {
        title: "Deep Work",
        authorName: "Cal Newport",
        releaseYear: 2016
    },
    {
        title: "1984",
        authorName: "George Orwell",
        releaseYear: 1949
    },
    {
        title: "The Great Gatsby",
        authorName: "F. Scott Fitzgerald",
        releaseYear: 1925
    }
];


function sortByYear(book1, book2) {
    if (book1.releaseYear === book2.releaseYear) {
        return 0
    } else if (book1.releaseYear < book2.releaseYear) {
        return -1
    } else {
        return 1
    }
}

const filteredBooks = books.filter(book => book.releaseYear <= 1950)


filteredBooks.sort(sortByYear);