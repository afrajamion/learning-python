'''
Exercise: Write a program which asks for a book title as input,
queries the books dictionary for the author, and prints the result
Stretch goal: alter the dictionary to associate authors to lists of books.
Ask the user for an author's name and return a list of books by that author
'''

# Exercise:
books = {"the handmaid's tale":"Margaret Atwood", "the hobbit":"J.R.R. Tolkien", "charlie and the chocolate factory":"Roald Dahl", "the shining":"Steven King", "the time machine":"H.G. Wells"}
title = input("Enter a book title: ")
print(f'{title} was written by: {books.get(title.lower(), "Unknown")}')


# Stretch goal:
books = {"j.r.r. tolkien":["The Hobbit", "The Lord Of The Rings", "The Silmarillion"], "roald dahl":["Charlie and the Chocolate Factory", "Matilda", "James and the Giant Peach"], "margaret atwood":["The Handmaid's Tale", "The Blind Assassin"]}
author = input("Enter an author: ")
print(f'Books by {author.title()}: {", ".join(books.get(author.lower(), []))}')