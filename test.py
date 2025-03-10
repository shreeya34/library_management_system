data={
    "Book": [
        {
            "book_id": 1,
            "title": "sss",
            "author_name": "George Orwell",
            "stock":4
        },
        {
            "book_id": 2,
            "title": "1984",
            "author_name": "George Orwell",
            "stock":4
        }

    ]
}

book_name = "1984"

for book in data["Book"]:
            breakpoint()
            if book['title'] == book_name:
                if book['stock'] > 0:
                    book['stock'] -=1
                    found = True
                    break
            if not found:
                print("Book not found out of stock")