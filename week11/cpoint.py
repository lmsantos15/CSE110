# 11 Prepare: Checkpoint

with open("books.txt") as checkpoint:
    for book in checkpoint:
        book = book.strip()

        print(book)
