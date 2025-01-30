numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(even_nums)

doubled_nums = list(map(lambda x: x * 2, even_nums))
print(doubled_nums)

sorted_nums = sorted(doubled_nums, key=lambda x: x, reverse=True)   #sorted() returns a new sorted list without modifying the original
print(f"Erste Option: {sorted_nums}")

doubled_nums.sort(key=lambda x:x, reverse=True)   #.sort() modifies the list in place and returns None
print(f"Zweite Option: {doubled_nums}")



books = [
    {"title": "Python Grundlagen", "author": "Max Mustermann", "year": 2020},
    {"title": "Datenstrukturen", "author": "Erika Musterfrau", "year": 2018},
    {"title": "Algorithmen", "author": "John Doe", "year": 2022}
]

# a)sort books by publication year
#key argument tells Python how to sort the items; 
#lambda book: book["year"] extracts the "year" value from each book dictionary
sorted_books = sorted(books, key=lambda book: book["year"])
print("\nSortierte Bücher:", sorted_books)

# b)filter books that were published after 2019
filtered_books = list(filter(lambda book: book["year"] > 2019, books))
print("Bücher nach 2019:", filtered_books)

# c)create a list with the titles of the books
titles = list(map(lambda book: book["title"], books))
print("Buchtitel:", titles)
